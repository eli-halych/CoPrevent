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
1. GET '/'
2. GET '/survey'
3. POST '/survey'
```

##### Endpoint description
```
1. GET '/'
DESCRIPTION:
    shows a world map with severail regions.
RETURNS: 
    a map? Folium?
```

```
2. GET '/survey'
DESCRIPTION:
    calls for a survey form. Is it necessary?
RETURNS: 
    a survey form? 
NOTES: 
    may be removed due to its potential unnecessity. Can be done with frontend?
```

```
3. POST '/survey'
DESCRIPTION: 
    calls an ML model,
    returns prediction/insight information based on request data.
REQUEST BODY: 
    {
      'country_region_code': ?,
      'country_region': ?,
      'sub_region_1': ?,
      'sub_region_2': ?,
      'date': ?,
      'still_on_lockdown': True/False
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