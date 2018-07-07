# blocc

blockchain thing in python lmao

[![Build Status](https://travis-ci.org/jmsv/blocc.svg?branch=master)](https://travis-ci.org/jmsv/blocc)

## Runnin

```bash
pipenv shell
pipenv install
make
```

## Example

```bash
$ python -m blocc

Start block:
 {
    "timestamp": "2018-07-07T01:13:45.684610",
    "prev": null,
    "index": 0,
    "data": {
        "message": "lol"
    },
    "hash": "a2f0b268af545817eac9435880af8ad46dd5a95c8ea0b8ff056f58f837f17105"
}

New block #1:
 {
    "timestamp": "2018-07-07T01:13:46.285459",
    "prev": "a2f0b268af545817eac9435880af8ad46dd5a95c8ea0b8ff056f58f837f17105",
    "index": 1,
    "data": {
        "random": 4905
    },
    "hash": "7e494211b4e2b891c970a441b23127d5e96c8903264af5dcc5f6de13998851ee"
}

New block #2:
 {
    "timestamp": "2018-07-07T01:13:47.787328",
    "prev": "7e494211b4e2b891c970a441b23127d5e96c8903264af5dcc5f6de13998851ee",
    "index": 2,
    "data": {
        "random": 7204
    },
    "hash": "9885516ab470a2aa3cce934bdea03845cf9a7ac06a2b5aac0cef294b96994c95"
}
```
