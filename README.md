Demo of a simple interaction between Python and Elixir using NATS.io

## How to use

1. start the NATS server, should listen at 0.0.0.0:4222
2. start the Elixir app with:
```
cd enpelixir
mix deps.get
mix run
```
3. start the Python app in a virtualenv with
```
python3 -m venv .venv
source .venv/bin/activate
export PYTHONPATH=$(pwd)
python3 -m pip install -r requirements.txt
python3 -m enp
```
