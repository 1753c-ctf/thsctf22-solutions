#include <openssl/evp.h>
#include <openssl/objects.h>
#include <stdio.h>

void my_callback(const OBJ_NAME *obj, void *arg)
{
	const EVP_MD* md = EVP_get_digestbyname(obj->name);
	printf("Digest: %s length: %x\n", obj->name, EVP_MD_size(md));
}

int list_hashes()
{
	void *my_arg;
	OpenSSL_add_all_digests();

	my_arg = NULL;
	OBJ_NAME_do_all(OBJ_NAME_TYPE_MD_METH, my_callback, my_arg);
	printf("===\n");
}

int main() {
	list_hashes();

	EVP_MD_CTX* mdctx = EVP_MD_CTX_new();
	const EVP_MD *md;
	char mess1[] = "Test Message\n";
	char mess2[] = "Hello World\n";
	unsigned char md_value[EVP_MAX_MD_SIZE];
	int md_len, i;

	OpenSSL_add_all_digests();

	md = EVP_get_digestbyname("SHA224");

	if(!md) {
	       printf("Unknown message digest\n");
	       exit(1);
	}
	for (long long i=0; i < 0xffffffff; i++){
		char* buff = (char*) &i;
		EVP_MD_CTX_init(mdctx);
		EVP_DigestInit_ex(mdctx, md, NULL);
		EVP_DigestUpdate(mdctx, &i, sizeof(i));
		EVP_DigestFinal_ex(mdctx, md_value, &md_len);
		if (md_value[0x1b] == 0 && md_value[0x1a] == 0 && md_value[0x19] == 0) {
			printf("%llx\n", i);
			break;
		}
	}

	printf("Digest is: ");
	for(i = 0; i < md_len; i++) printf("%02x", md_value[i]);
	printf("\n");
}

