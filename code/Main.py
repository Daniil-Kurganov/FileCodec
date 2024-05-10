from HammingCodec import hamming_codec_encode, hamming_codec_decode

string_filepath_source = 'C:/Users/User/PythonProjects/FileCodec/files/TXTFileEncode.txt'
string_filepath_result = 'C:/Users/User/PythonProjects/FileCodec/files/TXTFileDecode.txt'
bool_is_encode = False
file_source = open(string_filepath_source, encoding='utf8')
file_result = open(string_filepath_result, 'w', encoding='utf8')
for string_current_row in file_source:
    if bool_is_encode: file_result.write(hamming_codec_encode(string_current_row[:-1]) + '\n')
    else: file_result.write(hamming_codec_decode(string_current_row[:-1]) + '\n')
file_source.close()
file_result.close()
