#include <iostream>
#include <thread>
#include <vector>

#include <fmt/core.h>
#include <openssl/evp.h>

void show_hash(const unsigned char* md_value, int md_len) {
	fmt::print("hash: ");
	for(int i = 0; i < md_len; i++) fmt::print("{:02x}", md_value[i]);
	fmt::print("\n");
}

int hash_loop(uint64_t from, uint64_t to) {
	unsigned char md_value[EVP_MAX_MD_SIZE];
	EVP_MD_CTX* mdctx = EVP_MD_CTX_new();
	const EVP_MD* md;
	unsigned int md_len;
	md = EVP_get_digestbyname("SHA224");

	for (uint64_t i=from; i < to; i++) {

		EVP_MD_CTX_init(mdctx);
		EVP_DigestInit_ex(mdctx, md, NULL);
		EVP_DigestUpdate(mdctx, (char*) &i, sizeof(i));
		EVP_DigestFinal_ex(mdctx, md_value, &md_len);
		auto lsb = md_value[0x18];
		// 0x004013xx
		if (md_value[0x1b] == 0 &&
				md_value[0x1a] == 0x40 &&
				md_value[0x19] == 0x14 &&
				(lsb == 0xa4 || lsb == 0xa5 || lsb == 0xac ||
				 lsb == 0xb0 || lsb == 0xb5 || lsb == 0xbc ||
				 lsb == 0xbf || lsb == 0xc4 || lsb == 0xcb ||
				 lsb == 0xd0 || lsb == 0xd7 || lsb == 0xdc)) {
			fmt::print("hashed value: {:#x} (range {:#x}-{:#x})\n", i, from, to);
			for(int j = 0; j < sizeof(i); j++) fmt::print("{:02x}", ((unsigned char*)(&i))[j]);
			fmt::print("\n");
			show_hash(md_value, md_len);
			return 0;
		}
	}
	return 0;
}

int main() {
	std::vector<std::jthread> threads;
	uint64_t MAX_VAL = 0x10000000000;
	uint64_t chunk_size = MAX_VAL / std::thread::hardware_concurrency();
	for (int i = 0; i < std::thread::hardware_concurrency(); i++) {
		uint64_t min_val = chunk_size * i;
		uint64_t max_val = chunk_size * (i+1) - 1;
		fmt::print("thread[{}]: from {:#x} to {:#x}\n", i, min_val, max_val);
		threads.emplace_back(hash_loop, min_val, max_val);
	}
	threads[0].join();
	return 0;
}

