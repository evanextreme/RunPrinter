# RunPrinter

![Python package](https://github.com/evanextreme/RunPrinter/workflows/Python%20package/badge.svg)

## Description

RunPrinter is a minimal printer library which continuously prints console progress messages while an action is occurring. This is useful for complex data science operations using libraries such as `scipy` or `sklearn`, or any other complex operation where libraries are utilized. It will (eventually) be designed to overwrite the existing `print()` function call, acting as an interface with complete compatibility, allowing for an implementation with little to no changes.

## Why did you make this

My computer vision homework was frustrating me. I found it hard to tell whether or not my functions were actually running in a notebook, since they took a while to complete. I was also very bored.

## Usage

```python
from runprinter import Printer

printer = Printer(3)
printer.start("Reading image")
...
printer.restart("Categorizing image")
...
printer.restart("Printing image")
...
printer.stop()
```

Keep in mind, this library is in prerelease and calls are expected to change _drastically_ before its deemed ready.
