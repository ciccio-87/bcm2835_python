# bcm2835_python
Quick and dirty bcm2835 Python bindings

That's nothing more than a Swig interface and a Makefile to build (and install) everything.

Build & install (Raspbian):
- install swig3.0 (in Raspbian: apt-get install swig3.0)
- downloand bcm2835 library source (http://www.airspayce.com/mikem/bcm2835/), extract it
- git clone this repo in the bcm2835 source directory, cd into it
- make; sudo make install
