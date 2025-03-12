# pymt5linux

**Forked from [lucas-campagna/mt5linux](https://github.com/lucas-campagna/mt5linux). This is a up-to-date version which incorporates recent MT5 software updates. It works with Python 3.13.**

**As an alternative to the setup below, you can also opt to run a Docker image of MT5 with x11/noVNC remote access. Check out [mt5docker](https://github.com/hpdeandrade/mt5docker) for details.**

## Requirements

1. [Wine](https://www.winehq.org)

2. [Python Windows](https://www.python.org)

3. [MT5 software](https://www.metatrader5.com)

...or check out the [MT5 Linux user guide](https://www.metatrader5.com/en/terminal/help/start_advanced/install_linux).

## Install

1. Install [Wine](https://wiki.winehq.org/Download).

2. Install [Python for Windows](https://www.python.org/downloads/windows) on Linux with the help of Wine.

3. Find the path to `python.exe`.

4. Install [MT5](https://www.mql5.com/en/docs/integration/python_metatrader5) library on your **Windows** Python version.

```
pip install MetaTrader5
```

5. Install this package on both **Windows** and **Linux** Python versions:

```
pip install pymt5linux
```

## How To Use

Follow the steps:

On **Windows** side:

1. Open the MT5 client.

2. Start the server on a terminal:

```
python -m pymt5linux <path/to/python.exe>
```

On **Linux** side:

3. Make your scripts/notebooks as you did with MT5:

```python
# import the package
from pymt5linux import MetaTrader5

# connect to the server
mt5 = MetaTrader5(
    # host = "localhost" (default)
    # port = 18812       (default)
)

# use as you learned from https://www.mql5.com/en/docs/integration/python_metatrader5
mt5.initialize()
mt5.terminal_info()
mt5.copy_rates_from_pos("GOOG", mt5.TIMEFRAME_M1, 0, 1000)

# don't forget to shutdown
mt5.shutdown()
```

4. Be happy!

On step 2 you can provide the port, host, executable, etc... just type `python -m pymt5linux --help`.