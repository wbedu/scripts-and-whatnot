#!/bin/bash

set -e
set -o pipefail
echo "This script is intended for testing purposes only. The dracut-crypt-ssh and dropbear repositories are not widely reviewed, so use at your own risk."
read -p "Press Enter to proceed or Ctrl+C to cancel..."
git clone https://github.com/dracut-crypt-ssh/dracut-crypt-ssh.git
git clone https://github.com/mkj/dropbear.git
dnf install libblkid-devel
sudo grubby --update-kernel=ALL --args="rd.neednet=1"
pushd dropbear
./configure
make -j$(nproc)
cp ./dropbear* /sbin
popd
pushd dracut-crypt-ssh
./configure
make -j$(nproc)
make install
