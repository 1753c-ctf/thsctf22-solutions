all: cracko hashcheck

cracko: crack.cpp
	g++ --std=c++20 -O3 -g -lfmt -lcrypto crack.cpp -o cracko

hashcheck: hashcheck.c
	gcc -lcrypto hashcheck.c -o hashcheck

clean:
	@rm -f cracko hashcheck
