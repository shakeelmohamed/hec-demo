# Splunk HEC .Conf 2016 demo

Description:

Takes a picture from your Macbook's webcam, converts the images to ASCII art, then sends it to Splunk's HTTP Event Collector!

Requirements:

* OS X
* Homebrew
* Splunk 6.3+
* Python 2.7

Usage:

```shell
brew install imagesnap jp2a
export HEC_URI="http(s)://<host>:<port>"
export HEC_TOKEN="<token>"

python program.py snapshot.jpg
```