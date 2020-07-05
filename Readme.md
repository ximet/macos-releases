# MacOS-releases [![Build Status](https://travis-ci.com/ximet/macos-releases.svg?branch=master)](https://travis-ci.com/ximet/macos-releases.svg?branch=master)

> Get the name and version in a tuple  of a macOS (OSX) release from Darwin
> For instance: "20.0.0" -> ('Big Sur', '11.0 beta 1')

## Install

```
$ pip install macos-releases==1.0
```

## Usage

```python
import getMacOSRelease

# Your current macOS system

getMacOSRelease();
//=> ('Catalina', '10.15.5')

# Beta version
getMacOSRelease('20.0.0);
//=> ('Big Sur', '11.0 beta 1')
```

## API

### getMacOSRelease(release?)

#### release

Type: `string`

By default, the current operating system is used, but you can supply a custom [Darwin kernel version](https://en.wikipedia.org/wiki/Darwin_%28operating_system%29#Release_history)

