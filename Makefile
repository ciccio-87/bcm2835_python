PYV:=$(shell python -c "import sys;t='{v[0]}.{v[1]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)");
PYTHON:=python$(shell echo $(PYV))

all:
	swig3.0 -python bcm2835.i
	gcc -c -fpic bcm2835_wrap.c ../src/bcm2835.c -I /usr/include/$(PYTHON)
	gcc -shared bcm2835.o bcm2835_wrap.o -o _bcm2835.so
install:
	cp bcm2835.py _bcm2835.so /usr/local/lib/$(PYTHON)/dist-packages/
clean:
	rm *.o *.py *.so *.c
uninstall:
	rm /usr/local/lib/$(PYTHON)/dist-packages/bcm2835.py
	rm /usr/local/lib/$(PYTHON)/dist-packages/_bcm2835.so
