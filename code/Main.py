import docx
from HammingCodec import hamming_codec_encode, hamming_codec_decode

string_filepath_source = 'C:/Users/User/PythonProjects/FileCodec/files/WordFileEncode.docx'
string_file_type = string_filepath_source[string_filepath_source.rfind('.') + 1:]
string_filepath_result = string_filepath_source[:string_filepath_source.rfind('/') + 1] + 'WordFileDecode' + '.' + string_file_type
bool_operation_is_encode = False
if string_file_type == 'txt':
    file_source = open(string_filepath_source, encoding='utf8')
    file_result = open(string_filepath_result, 'w', encoding='utf8')
    for string_current_row in file_source:
        if bool_operation_is_encode: file_result.write(hamming_codec_encode(string_current_row[:-1]) + '\n')
        else: file_result.write(hamming_codec_decode(string_current_row[:-1]) + '\n')
    file_source.close()
    file_result.close()
elif string_file_type == 'docx':
    file_source, file_result = docx.Document(string_filepath_source), docx.Document()
    for paragraph_current in file_source.paragraphs:
        if bool_operation_is_encode: file_result.add_paragraph(hamming_codec_encode(paragraph_current.text))
        else: file_result.add_paragraph(hamming_codec_decode(paragraph_current.text))
    file_result.save(string_filepath_result)
