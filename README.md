ffmpeg is required for script
```
# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg
```
whisper require python 3.11

for gpu usage, install cuda drive and torch with matched version

this thread may help for torch error

[AssertionError: Torch not compiled with CUDA enabled #30664](https://github.com/pytorch/pytorch/issues/30664#issuecomment-757431613)

create venv with python 3.11
```
py -3.11 -m venv venv_py311
```
