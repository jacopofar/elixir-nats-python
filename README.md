Demo of a simple interaction between Python and Elixir using NATS.io

## How to run

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

## Issues

Surprisingly, the Elixir part was much simpler to write.
The Python library makes it quite complex to listen and write at the same time, there's no "wait with timeout" option, nor greenlet.
I had to use threading (yep!) and it hangs forever when trying to terminate it so I can't close gracefully.

The alternative is to use the async python library which requires a lot of boilerplate plus the usual pain of asynchronous python. Still satisfied with the Elixir part, though.
