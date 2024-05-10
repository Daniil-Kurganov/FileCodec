import docx
from HammingCodec import hamming_codec_encode, hamming_codec_decode

file_source, file_result = docx.Document('C:/Users/User/PythonProjects/FileCodec/files/WordFileEncode.docx'), docx.Document()
for paragraph_current in file_source.paragraphs:
    file_result.add_paragraph(hamming_codec_decode(paragraph_current.text))
file_result.save('C:/Users/User/PythonProjects/FileCodec/files/WordFileDecode.docx')