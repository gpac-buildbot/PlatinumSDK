#!/bin/sh -e
if [ $# -ne 1 ] ; then
  echo "Usage: `basename $0` scons_platform"
  exit 1
fi

cd Platinum
scons -j 4
if [ $? != 0 ] ; then
	exit 1
fi
mkdir -p ../../../gpac_public/extra_lib/lib/gcc
cp Build/Targets/$1/Debug/*.a ../../../gpac_public/extra_lib/lib/gcc
