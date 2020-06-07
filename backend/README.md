## Documentation

### Table of contents
1. [Errors](#errors)
2. [Endpoints](#endpoints)
3. [Endpoint description](#endpoint-description)
4. [Tests](#tests)

### Errors
```
400 - Bad Request
422 - Unprocessabel Enityt 
```

### Endpoints
```
1. POST '/survey'
```

##### Endpoint description

```
1. POST '/survey'
DESCRIPTION: 
    calls an ML model,
    returns prediction/insight information based on request data.
REQUEST BODY: 
    {
      'country_region_code': 'US',
      'look_froward_days': 3
    }
RETURNS: 
    {
      'country_region_code': 'US',
      'prediction': ?,
      'message': ?,
      'trend': 'increasing' OR 'decreasing',
      'success': True
    }, 200
```

Region codes are described here:
[`./datasets/README.md`](./datasets/README.md)

### Tests
All endpoints are covered with unittests. To call tests, call the main test class
in [`./test.py`](./test.py)