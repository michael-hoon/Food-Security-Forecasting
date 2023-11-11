# Install guide for webappp

## Requirements
- cloned repo
- `python3`

## Steps for Linux/MacOS Users
1. Downloading requirements
```sh
./setup.sh
```
2. Running webapp
```sh
./startup.sh
```

## Steps for Windows Users

1. Downloading requirements
```sh
python -m venv .venv
python -m pip install -r requirements.txt
```

2. Running webapp
```sh
. .venv/Scripts/activate
flask run
```
