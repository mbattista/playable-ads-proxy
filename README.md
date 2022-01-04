# Playable Ads Proxy
[Evan Kohilas](https://github.com/ekohilas/playable-ads) has a fantastic presentation about playable ads and what they really are.
This had me also dig into it and wrote up some steps to reproduce it and some features I want to impement later.

As of now, this project will only replace ads served by the unity ad plattform, but I will try to get more ad plattforms working.

### Installation
1. Install MITMProxy on a device in your network, e.g. a raspberry pi or a laptop. [The recommended way would be to use pipx](https://docs.mitmproxy.org/stable/overview-installation/#installation-from-the-python-package-index-pypi)
2. Start the mitmproxy and use the unityaddon from this project (eg `mitmweb --web-host 0.0.0.0 -s <PATH-TO-THE-ADDON>`)
3. Set the proxy in your wifi connection.
4. Visit mitm.it while in the proxy and install the certificate from the proxy
5. The next ad from an unitygame will be replaced by with the rss feed from `tagesschau.de`, this could be replaced in the unityaddon with any site that could run in an iframe.
6. Still get the reward for watching the "Ad" afterwards

