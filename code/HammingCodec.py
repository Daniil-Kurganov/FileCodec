import math

def calculation_of_correction_bits(list_positions_of_correction_bits: list, list_code_underword: list) -> str:
    '''Вычисление корректирующих битов в кодовых подсловах'''
    global int_n
    for int_position_of_correction_bit in list_positions_of_correction_bits:
        int_current_correction_bit = 0
        for int_position_of_tail_bit in range(int_position_of_correction_bit * 2, int_n, (int_position_of_correction_bit + 1) * 2):
            for int_bit_subblock_position in range (int_position_of_tail_bit - int_position_of_correction_bit, int_position_of_tail_bit + 1):
                if list_code_underword[int_bit_subblock_position][0] != 'b':
                    int_current_correction_bit = int(ord(str(int_current_correction_bit)) ^ ord(str(list_code_underword[int_bit_subblock_position])))
        list_code_underword[int_position_of_correction_bit] = str(int_current_correction_bit)
    return ''.join(list_code_underword)
def changing_the_bit(string_bit: str) -> str:
    '''Заменяет бит на противоположный'''
    return str((int(string_bit) + 1) % 2)
def cutting_code_subword_to_information_word(string_code_underword: str) -> str:
    '''Выбивание корректирующих битов из кодовых подслов и преобразование их в информационные'''
    list_current_information_underword = []
    for int_position_of_bit in range(1, int_n + 1):
        if (int_position_of_bit & (int_position_of_bit - 1) == 0): pass
        else: list_current_information_underword.append(string_code_underword[int_position_of_bit - 1])
    return ''.join(list_current_information_underword)
def hamming_codec_encode(string_input_text_real: str) -> str:
    '''Кодирование текста и представление в виде числа'''
    global int_r, int_n, int_k
    string_input_text_binary = bin(int.from_bytes(string_input_text_real.encode(), 'big'))[2:]
    list_informaion_underwords, list_code_underwords = [], []
    int_count_of_zeros = 0
    if len(string_input_text_binary) > int_k:
        for iteration in range(1, math.ceil(len(string_input_text_binary) / int_k)):
            list_informaion_underwords.append(string_input_text_binary[iteration * int_k - int_k:iteration * int_k])
        if len(string_input_text_binary) % int_k != 0:
            int_count_of_zeros = int_k - (
                        len(string_input_text_binary) - (int_k * (len(string_input_text_binary) // int_k)))
            list_informaion_underwords.append(
                ('0' * int_count_of_zeros) + string_input_text_binary[-(int_k - int_count_of_zeros):])
        else:
            list_informaion_underwords.append(string_input_text_binary[-int_k:])
    else:
        int_count_of_zeros = int_k - len(string_input_text_binary)
        list_informaion_underwords.append(('0' * int_count_of_zeros) + string_input_text_binary)
    for string_information_underword in list_informaion_underwords:
        list_code_underword, list_positions_of_correction_bits = [], []
        int_posotion_of_bits = 0
        for int_position_of_bit in range(1, int_n + 1):
            if (int_position_of_bit & (int_position_of_bit - 1) == 0):
                list_code_underword.append('b' + str(int_position_of_bit))
                list_positions_of_correction_bits.append(len(list_code_underword) - 1)
            else:
                list_code_underword.append(string_information_underword[int_posotion_of_bits])
                int_posotion_of_bits += 1
        list_code_underwords.append(calculation_of_correction_bits(list_positions_of_correction_bits, list_code_underword))
    return ''.join(list_code_underwords) + '.' + str(int_count_of_zeros)
def hamming_codec_decode(string_input_code_word: str) -> str:
    '''Декодирование текста из числа кодового слова'''
    global int_n
    int_point_of_trimm = string_input_code_word.find('.')
    string_code_word = string_input_code_word[:int_point_of_trimm]
    int_count_of_zeros = int(string_input_code_word[int_point_of_trimm + 1:])
    list_informaion_underwords = []
    list_code_underwords = [string_code_word[int_current_index_of_start: int_current_index_of_start + 31] for int_current_index_of_start in
                            range(0, len(string_code_word), 31)]
    for string_code_underword in list_code_underwords:
        string_current_information_underword = cutting_code_subword_to_information_word(string_code_underword)
        list_informaion_underwords.append(string_current_information_underword)
    if int_count_of_zeros > 0: list_informaion_underwords[-1] = list_informaion_underwords[-1][int_count_of_zeros:]
    string_output_text_binary = ''.join(list_informaion_underwords)
    return int(string_output_text_binary, 2).to_bytes((int(string_output_text_binary, 2).bit_length() + 7) // 8, 'big').decode()

int_r, int_n, int_k = 5, 31, 26
