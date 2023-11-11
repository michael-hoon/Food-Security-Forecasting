# Install guide for webappp

## Requirements
- `python3`

## Steps for Linux/MacOS Users
1. Downloading requirements (assuming you have cloned the repo already)
```sh
./setup.sh
```
2. Running webapp
```sh
./startup.sh
```

## Steps for Windows Users

1. Downloading requirements (assuming you have cloned the repo already)
```sh
python -m venv .venv
python -m pip install -r requirements.txt
```

2. Running webapp
```sh
. .venv/Scripts/activate
flask run
```
