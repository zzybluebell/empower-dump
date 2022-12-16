# Coding Assignment 

## File Structure

```
├── /app.py         # Flask server consists of 3 endpont RestAPI 'login', 'summary' & 'rank'
├── /test_app.py    # Unit testing covers all three endpoints with succeffull and fail testcases. run unit test by typing command "python -m pytest"
├── /start.sh       # script file in the root folder that builds the dependencies and then starts the server.

``` 

## API Server documentation

### `login`: http://127.0.0.1:5000/login

1. This `login` endpoint need two paramenters: `username` & `password` 
2. When it login the server, it will use username and password,
3. Return `successful` if login successful, return `fail` if username or password is invalid.

### `summary` http://127.0.0.1:5000/summary

1. This `summary` endpoint needs one parameter `date`, it queries the login user's activity by the given date.
2. Return `error message` if has not logged in or date is invalid, return empty string if no activity found
3. if successful, return patient' `steps`, `distance`, `calorie burn` and `active minutes` in the given date.

### `rank` http://127.0.0.1:5000/rank
1.  This `rank` endpoint does not need parameter.
2.  Returns a list of `Patient.username`
3.  The list is sorted by the total number of steps which has been accumulated throughout the history, and the steps is in `descending` order 