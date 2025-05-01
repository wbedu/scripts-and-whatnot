#!/bin/bash

set -e
host=$1
port="${port:=22}"

if [ -z "$host" ]; then
  echo "Error: Host is not defined."
  echo "Usage: $0 <host> [port]"
  exit 1
fi


hostkeyPath=$(mktemp -d)
pushd $hostkeyPath
ssh-keyscan -p $port -t rsa,ed25519 $host \
  | awk '{$1=$1; print $2, $3}' \
  > cleaned_keys.pub > hostkeys.pub;
while read key; do
  ipa host-mod $host --sshpubkey="$key"
done < hostkeys.pub
popd
rm -rf $hostkeyPath