import requests
import json


def test_post_headers_body_json():
    url = 'http://0.0.0.0:5000/resource_optimizer'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {"capacity": 1150, "hours": 1}

    # convert dict to json by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

    # Validate response headers and body contents, e.g. status code.
    assert resp.status_code == 200
    resp_body = resp.json()
    assert resp_body['output'][0]['total_cost'] == "$10150"
    assert resp_body['output'][1]['total_cost'] == "$9520"
    assert resp_body['output'][2]['total_cost'] == "$8570"

    # print response full body as text
    print(resp.text)
