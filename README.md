# HMLink

A Bridge between Houdini and Maya

Tutorial:

https://youtu.be/-RyY08267lY

## Houdini Setup

## Package Install (JSON)

Find `hmlink.json` in `HMLink/Houdini`

Edit `"hmlink": "C:/Users/otaku/Documents/GitHub/HMLink/Houdini"` to your path.

Copy and paste this json file to Houdini package path, by default it is in 

```
C:\Program Files\Side Effects Software\Houdini XX.X.XXX\packages
```

### Manual Install

Edit `Houdini.env`, add:

```
HOUDINI_PATH = "C:/HMLink/Houdini;&"
PYTHONPATH = "C:/HMLink/Houdini;&"
```

## Create Shelf in Houdini

run in houdini python shell:

```
import hml_shelf
import importlib
importlib.reload(hml_shelf)
hml_shelf.shelf()

```

Click the `+` button on the shelves, and you can find `HMLink` in shelves.

## How to use

You need to select a node before you export and import.

## Maya Setup

Drag and drop the `Maya/hml.mel` into Maya viewport.
