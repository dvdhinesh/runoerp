Developer Utility tool to run openerp server, upgrade all modules...

Binaries will be available for debian precise. Currently supports linux and static server paths. 
Dynamic paths will be added soon. Needs postgres available on the same machine.

Build available for Debian precise:

For apt-get:

sudo add-apt-repository ppa:dvdhinesh-mail/runoerp

sudo apt-get update

sudo apt-get install python-runoerp

If fails:

Download source, build and install for your version/architecture:

sudo apt-get install python-stdeb

cd runoerp && python setup.py --command-packages=stdeb.command bdist_deb

will give deb_dist and you can install by clicking (running) .deb file created.
