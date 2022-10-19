#!/bin/bash
tor &
curl -s --socks5-hostname localhost:9050 http://thsctf2tyszoftrlkyirbkmfgqhlp2amg64ry5h3hiqstruqpdmk42id.onion | grep password
images=$(curl -s --socks5-hostname localhost:9050 http://thsctf2tyszoftrlkyirbkmfgqhlp2amg64ry5h3hiqstruqpdmk42id.onion/images/ | grep jpg | cut -f 2 -d '"' | tr '\n' ' ')
for image in $images
do
    echo $image
    curl -s --socks5-hostname localhost:9050 http://thsctf2tyszoftrlkyirbkmfgqhlp2amg64ry5h3hiqstruqpdmk42id.onion/images/$image -o $image
    steghide extract -p LEM -sf $image
done
cat flag.txt
