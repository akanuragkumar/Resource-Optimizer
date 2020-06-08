# Hiring_assignment_2

## Quickstart

To work in a sandboxed Python environment it is recommended to install the app in a Python [virtualenv](https://pypi.python.org/pypi/virtualenv).

1. Install dependencies

    ```bash
    $ cd /path/to/hiring_assignment_2
    $ pip install -r requirements.txt
    ```
2. Run server

   ```bash
   $ python app/runserver.py
   ```

   View at http://127.0.0.1:5000
   
## Project Structure

### Backend 
```shell
hiring_assignment_2
├── app                                         # contains application files
│   ├── resource_optimizer──────┐               # contains resource files for API
│   └── runserver               │               # serves API and manages the requests
│                               └── app.py      # main API file 
├── test_api                                    # test suites for pytest
└── __init__                                    # __init__ file
   
```
## Test cases
   ```bash
   $ pytest
   ```

## API Documentation 

### `resource_optimizer` 

1. `POST /resource_optimizer` 

```json
 application/json - {"capacity":1150,"hours":1}
```
##### `response`

```json
status- 200 OK
 {
  "output": [
    {
      "machines": [
        [
          "8Xlarge",
          7
        ],
        [
          "Xlarge",
          1
        ],
        [
          "large",
          1
        ]
      ],
      "region": "New York",
      "total_cost": "$10150"
    },
    {
      "machines": [
        [
          "8Xlarge",
          7
        ],
        [
          "large",
          3
        ]
      ],
      "region": "India",
      "total_cost": "$9520"
    },
    {
      "machines": [
        [
          "8Xlarge",
          7
        ],
        [
          "Xlarge",
          1
        ],
        [
          "large",
          1
        ]
      ],
      "region": "China",
      "total_cost": "$8570"
    }
  ]
}
```
