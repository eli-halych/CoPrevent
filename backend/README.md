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
      'start_date': '2020-03-01',
      'end_date': '2020-05-01'
    }
RETURNS: 
    personalized prediction, 
    success status, 
    a message, 
    other miscellaneous information
    and a status code.
NOTES:
    request body details are based on reagion codes from another API?
```

### Tests
All endpoints are covered with unittests. To call tests, call the main test class
in [`./test.py`](./test.py)