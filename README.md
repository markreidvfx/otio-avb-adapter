OpenTimelineIO Avid Bin (AVB) Adapter
=====================================

[![Supported VFX Platform Versions](https://img.shields.io/badge/vfx%20platform-2018--2021-lightgrey.svg)](http://www.vfxplatform.com/)
![Supported Versions](https://img.shields.io/badge/python-2.7%2C%203.7%2C%203.8%2C%203.9%2C%203.10-blue)
[![Run tests](https://github.com/markreidvfx/otio-avb-adapter/actions/workflows/ci.yaml/badge.svg)](https://github.com/markreidvfx/otio-avb-adapter/actions/workflows/ci.yaml)

This adapter uses [pyavb](https://github.com/markreidvfx/pyavb) for reading AVB files

Testing for Development
-----------------------

```bash
# In the root folder of the repo
pip install -e .

# Test adapter
otioconvert -i some_timeline.avb -o some_timeline.ext
```
