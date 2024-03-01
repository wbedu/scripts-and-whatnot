#!/usr/bin/env bash

# switch used to determine if i am going to use an ssh proxy or not
# used with ssh_config MATCH statement
# assume we use a proxy on default
# does add some latency when connecting

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <ip-to-test> <value-to-check> <comma-separated-list>"
    exit 1
fi

ip_to_test="$1"
value_to_check="$2"
valid_hosts="$3"

# Split the valid_hosts into an array
IFS=',' read -ra hosts_array <<< "$valid_hosts"

for item in "${hosts_array[@]}"; do
    echo $item
    if [ "$item" = "$value_to_check" ]; then
        echo $item is a match
        public_ip=$(ssh jumphost "echo \$SSH_CONNECTION | awk '{print \$1}'")
        if [ "$public_ip" = $ip_to_test ]; then
        	# local no use proxy
        	exit 0
        fi
        break
    fi
done

# use proxy
exit 1
