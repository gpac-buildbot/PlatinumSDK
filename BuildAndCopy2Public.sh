#!/bin/sh -e
if [ $# -ne 1 ] ; then
  echo "Usage: `basename $0` scons_platform"
  exit 1
fi
set +e
cd Platinum
scons -j 4
ret=$?
# some might fail but the useful .a still be there, so don't exit if errors
# if [ $? != 0 ] ; then
# 	exit 1
# fi
mkdir -p ../../../gpac_public/extra_lib/lib/gcc
cp -av Build/Targets/$1/Debug/*.a ../../../gpac_public/extra_lib/lib/gcc

exit $ret