# pymt5linux

**Forked from https://github.com/hpdeandrade/pymt5linux.
**work with  Python >= 3.9**

pip install git+https://github.com/tradeset/py3mt5linux.git



**As an alternative to the setup below, you can also opt to run a Docker image of MT5 with x11/noVNC remote access. Check out [mt5docker](https://github.com/hpdeandrade/mt5docker) for details.**

## How To Use

1. Install (as per [MT5 Linux user guide](https://www.metatrader5.com/en/terminal/help/start_advanced/install_linux)):
    * [Wine](https://www.winehq.org) in your Linux machine.
    * [Python for Windows](https://www.python.org) inside Wine.
    * [MT5 software](https://www.metatrader5.com) inside Wine.
    
2. Install MetaTrader5 package inside your Wine Python installation.

```
pip install MetaTrader5
```

3. Install pymt5linux package in both Wine and Linux Python versions.

```
pip install pymt5linux
```

4. Establish the connection.

* Open the MT5 terminal in Wine.

* Run the MT5 server in Wine.

`python -m pymt5linux <path/to/python.exe>`,

or if you want to specify the host and port:

`python -m pymt5linux --host localhost --port 8001 <path/to/python.exe>`

* Run your Linux script.

```python
# import the package
from pymt5linux import MetaTrader5

# establish the connection
mt5 = MetaTrader5()

# or if you specified the host and port in the previous step:
mt5 = MetaTrader5(host="localhost", port=8001)
```

5. Make sure you test with a DEMO account first, then have fun!

Most importantly, see MetaQuotes' [official documentation](https://www.mql5.com/en/docs/python_metatrader5).