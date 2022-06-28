## OpenTimelineIO Avid Bin (AVB) Adapter

This adapter uses [pyavb](https://github.com/markreidvfx/pyavb) for reading AVB files

## Testing for development
```bash
# In the root folder of the repo
pip install -e .

# Test adapter
otioconvert -i some_timeline.avb -o some_timeline.ext
```
