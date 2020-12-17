# oscer

A **very** simple command line OSC message sender.

## Installation

You will need Python>=3.7 and pythonosc.

The simplest way to install is using pip:

`$ pip install oscer`

## Example

```
$ oscer
usage: oscer [-h] [--ip IP] [--port PORT] OSC_ADDR [OSC_VALUE ...]

positional arguments:
  OSC_ADDR     OSC address to send
  OSC_VALUE    OSC values

optional arguments:
  -h, --help   show this help message and exit
  --ip IP      The ip of the OSC server
  --port PORT  The port the OSC server is listening on
```

So:

`$ oscer --ip localhost --port 57120 /hello argument1 "another argument" 3`

It will try to guess the data type correctly, otherwise send as a string argument.

You can use the environment variables `OSCER_HOST` and `OSCER_PORT` also, so you don't need to specify the hostname and port every time.
