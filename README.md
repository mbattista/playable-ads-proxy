# Playable Ads Proxy
[Evan Kohilas](https://github.com/ekohilas/playable-ads) has a fantastic presentation about playable ads and what they really are.
This had me also dig into it and wrote up some steps to reproduce it and some features I want to impement later.

As of now, this project will only replace ads served by the unity ad plattform, but I will try to get more ad plattforms working.

### Installation
1. Install MITMProxy on a device in your network, e.g. a raspberry pi or a laptop. [The recommended way would be to use pipx](https://docs.mitmproxy.org/stable/overview-installation/#installation-from-the-python-package-index-pypi)
2. Start the mitmproxy with the `unityaddon.py` from this project (eg `mitmweb --web-host 0.0.0.0 -s <PATH-TO-THE-ADDON>`)
3. Set the proxy in your wifi connection.
4. Visit mitm.it while in the proxy and install the certificate from the proxy
5. The next ad from an unitygame will be replaced by with the rss feed from `tagesschau.de`, this could be replaced in the `unityaddon.py` with any site that could run in an iframe. You need to replace `http%3A%2F%2Fus1.rssfeedwidget.com%2Fgetrss.php%3Ftime%3D1641319246119%26amp%3Bx%3Dhttps%253A%252F%252Fwww.tagesschau.de%252Fxml%252Frss2%252F%26amp%3Bw%3D1000%26amp%3Bh%3D600%26amp%3Bbc%3D333333%26amp%3Bbw%3D1%26amp%3Bbgc%3Dtransparent%26amp%3Bm%3D20%26amp%3Bit%3Dtrue%26amp%3Bt%3D%28default%29%26amp%3Btc%3D333333%26amp%3Bts%3D15%26amp%3Btb%3Dtransparent%26amp%3Bil%3Dtrue%26amp%3Blc%3DE1E0FF%26amp%3Bls%3D16%26amp%3Blb%3Dtrue%26amp%3Bid%3Dtrue%26amp%3Bdc%3DF5F5F5%26amp%3Bds%3D14%26amp%3Bidt%3Dtrue%26amp%3Bdtc%3D284F2D%26amp%3Bdts%3D12` with any other site that allows to run in a frame and you like to read for 30 seconds. But remember to [URIEncode](https://www.urlencoder.org/) the URL to the site.
6. Still get the reward for watching the "Ad" afterwards

