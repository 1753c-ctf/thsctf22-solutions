from hashlib import md5
import itertools

product = itertools.product("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=?,.'[]\{\}", repeat=2)

data ={
    "5b79c40fa7c2bd12dd2df53c4a2b6836": 0, 
    "6a65edb0cc17d66c677814115b1477f5": 0, 
    "c3ee2af7ca7bbe492f11cf36a6a7cea7": 0, 
    "330d125217f5ee4aa36e0fbc9a4df9dc": 0, 
    "3c26ded50693926656dbaeb1c67eb876": 0, 
    "1696ca97569817cf0410465c415c3263": 0, 
    "e53125275854402400f74fd6ab3f7659": 0, 
    "4b8230ce4e3bf83e6ca468783d99aaaf": 0, 
    "5123dd8b087b644fdb8f8603acd1bad4": 0, 
    "b5f3729e5418905ad2b21ce186b1c01d": 0, 
    "fc85e0e9e785e1ac37df34f744769c5f": 0, 
    "5fcfcb7df376059d0075cb892b2cc37f": 0, 
    "baceebebc179d3cdb726f5cbfaa81dfe": 0, 
    "0d149b90e7394297301c90191ae775f0": 0, 
    "ff108b961a844f859bd7c203b7366f8e": 0, 
    "1742a6a41222e1c2f36c5fb7b6396fe3": 0, 
    "5526021d73a11a9d0775f47f7e4754c4": 0, 
    "ac8242942174ddadc98c2d81e968d8e7": 0, 
    "6fbd8724ad707b07e28acb57fa567a2a": 0, 
    "89e6d2b383471fc370d828e552c19e65": 0, 
    "4605f628f91de21e4b5f9433f46e29eb": 0, 
    "13e9f0f7ec00ce86e65f26031d80b7ba": 0, 
    "db26ee047a4c86fbd2fba73503feccb6": 0, 
    "0a3d72134fb3d6c024db4c510bc1605b": 0, 
    "ca4da36c48be1c0b87a7d575c73f6e42": 0, 
    "5b54c0a045f179bcbbbc9abcb8b5cd4c": 0, 
    "8526b80a8550c1fffdf9295659572605": 0
}

for group in product:
    hash = md5(''.join(map(str, list(group))).encode('utf-8')).hexdigest()
    if hash in data.keys():
        data[hash] = ''.join(map(str, list(group)))

print(''.join(map(str,data.values())))
