# DOC

### Install
python version 3.9

```sh
python3.9 -m venv ./venv
source ./venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r ./requirements.txt
```

### start api server(SQL runner)
```sh
uvicorn --port 8000 api_server:app --reload
```

### testing
```sh
python ./test_post_requests.py async 50 > test_result.txt
```

### result
```sh
vi test_result.txt
```
OR
```sh
code test_result.txt
```