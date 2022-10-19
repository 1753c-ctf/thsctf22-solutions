In the file "pcap" communication between two people is contained (rocketchat) and the encrypted packed file message_2.zip is sent.
To find a flag:
1. Extract the Wireshark, tcpflow, foremost ....
2. Crack the password of the message_2.zip file (zip2john, john -> password: hacker) - używając 'tcpflow -r' użyć: zip -FFv data.zip --out fixed.zip
3. Unpack the message.zip file
4. In the received file, find the flag encoded in the Brainfuck language:

++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>++++++++++++++.------------.+++++++++++.----------------.>----------------.<+++.>+++++++++++++++++++++++++++++++++++++++.<<++++++++++++++++++.>>-------------.--.+++++++++++++.<+++++++++++++++++++++++++.>-------.<<.>+++.<.+++++++.--.>---.++++.<-.>>----.<----.>--.<<---.>>++++++++++.<<++.>.<---.>>--------.<.<+++.+.>>++++.<<+++.>+++++++++.>+++++++++++.

decoder: https://www.dcode.fr/brainfuck-language

Flag: THSCTF{0nly_r0b075_c4n_l1v3_0n_34r7h}

There is a trick:
AHR0cHM6Ly90aW55LnBsL2gyeHZr -> https://tiny.pl/h2xvk -> Rick Roll ;)
