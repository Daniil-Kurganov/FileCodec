# string_filepath = 'C:/Users/User/PythonProjects/FileCodec/files/TXTFile.txt'
# file = open(string_filepath, encoding = 'utf8')
# list_encode_result = []
# for string_current_row in file:


def text_from_bits(string_bits: str, bool_encode_type: bool) -> str:
    '''Преобразование бинарной последовательности в текст'''
    int_string_number = int(string_bits, 2)
    if bool_encode_type: return int_string_number.to_bytes((int_string_number.bit_length() + 7) // 8, 'big')
    else: return int_string_number.to_bytes((int_string_number.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass')
def text_to_bits(string_text: str, bool_encode_type: bool) -> str:
    '''Преобразование текста в бинарный вид'''
    encoding, errors = 'utf-8', 'surrogatepass'
    if bool_encode_type: bits = bin(int.from_bytes(string_text, 'big'))[2:]
    else: bits = bin(int.from_bytes(string_text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

s_real_text = 'all'
s_code_word = text_to_bits(s_real_text, False) + '0010010'
s_write_code_word = text_from_bits(s_code_word, True)
print(s_write_code_word)
