from flask import Flask, request, jsonify
from healthcheck import HealthCheck

app = Flask(__name__)
app.config["DEBUG"] = True
data = []
response = { "output": []}

health = HealthCheck(app, "/healthcheck")

resource_capacity = {"large":10,"Xlarge":20,"2Xlarge":40,"4Xlarge":80,"8Xlarge":160,"10Xlarge":320}
region_1 = {"region":"New York","large":120,"Xlarge":230,"2Xlarge":450,"4Xlarge":774,"8Xlarge":1400,"10Xlarge":2820}
region_2 = {"region":"region_2","large":140,"Xlarge":0,"2Xlarge":413,"4Xlarge":890,"8Xlarge":1300,"10Xlarge":2970}
region_3 = {"region":"region_3","large":110,"Xlarge":200,"2Xlarge":0,"4Xlarge":670,"8Xlarge":1180,"10Xlarge":0}
regions = [region_1, region_2, region_3]


def resource_allocator(capacity, minima, region):
    resource_count = 0
    while int(capacity) >= int(resource_capacity[minima]):
        capacity = int(capacity) - int(resource_capacity[minima])
        resource_count += 1
    return capacity, resource_count, resource_count * region[minima]


def resource_cost(region, capacity, hours):
    resource = []
    total_cost, counter = 0, 0
    map_filter = dict((units, (float(region[units]) * int(hours)) / resource_capacity[units]) for units in resource_capacity)
    map_filter = {units: v for units, v in sorted(map_filter.items(), key=lambda item: item[1])}
    map_filter = {x: y for x, y in map_filter.items() if y != 0}

    keys = list(map_filter.keys())
    while capacity != 0:
        minima = keys[counter]
        (capacity,resource_count,cost) = resource_allocator(capacity, minima,region)
        counter += 1
        if resource_count>0:
            resource.append((minima,resource_count))
        total_cost += cost
    return response["output"].append({"region": region["region"], "total_cost": "$"+str(total_cost), "machines": resource})


@app.route("/resource_optimizer", methods=["POST"])
def resource_optimizer():
    data = request.json
    capacity = data['capacity']
    hours = data['hours']
    for region in regions:
        resource_cost(region, capacity, hours)
    return jsonify(response)


if __name__ == '__main__':
    app.run()
