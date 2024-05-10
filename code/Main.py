from HammingCodec import hamming_codec_encode, hamming_codec_decode

s = 'Я так хотел остаться...'
z = hamming_codec_encode(s)
print(z)
r = hamming_codec_decode(z)
print(r)