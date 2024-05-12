import docx
import openpyxl
from HammingCodec import hamming_codec_encode, hamming_codec_decode

if __name__ == '__main__':
    string_filepath_source = 'C:/Users/User/PythonProjects/FileCodec/files/ExcelFile.xlsx'
    string_file_type = string_filepath_source[string_filepath_source.rfind('.') + 1:]
    string_filepath_result = string_filepath_source[:string_filepath_source.rfind('/') + 1] + 'ExcelFileEncode' + '.' + string_file_type
    bool_operation_is_encode = True
    int_counter_done_operations = 0
    if string_file_type == 'txt':
        file_source = open(string_filepath_source, encoding='utf8')
        file_result = open(string_filepath_result, 'w', encoding='utf8')
        int_count_of_rows = sum(1 for string_current_row in file_source)
        file_source = open(string_filepath_source, encoding='utf8')
        for string_current_row in file_source:
            if bool_operation_is_encode: file_result.write(hamming_codec_encode(string_current_row[:-1]) + '\n')
            else: file_result.write(hamming_codec_decode(string_current_row[:-1]) + '\n')
            int_counter_done_operations += 1
            print((int_counter_done_operations / int_count_of_rows) * 100)
        file_source.close()
        file_result.close()
    elif string_file_type == 'docx':
        file_source, file_result = docx.Document(string_filepath_source), docx.Document()
        for paragraph_current in file_source.paragraphs:
            if bool_operation_is_encode: file_result.add_paragraph(hamming_codec_encode(paragraph_current.text))
            else: file_result.add_paragraph(hamming_codec_decode(paragraph_current.text))
            int_counter_done_operations += 1
            print((int_counter_done_operations / len(file_source.paragraphs)) * 100)
        file_result.save(string_filepath_result)
    elif string_file_type == 'xlsx':
        file_source, file_result = openpyxl.load_workbook(string_filepath_source, read_only=True), openpyxl.Workbook()
        for sheet_current_source in file_source.worksheets:
            print(file_source.worksheets.index(sheet_current_source))
            int_percentage_current_sheet_comlete = 100 / len(file_source.worksheets)
            sheet_current_result = file_result.create_sheet(title=sheet_current_source.title)
            for row_current_source in sheet_current_source.iter_rows():
                int_percentage_current_row_comlete = int_percentage_current_sheet_comlete / sheet_current_source.max_row
                for cell_current_source in row_current_source:
                    if cell_current_source.value is not None:
                        if bool_operation_is_encode:
                            sheet_current_result.cell(row=cell_current_source.row, column=cell_current_source.column,
                                                      value=hamming_codec_encode(str(cell_current_source.value)))
                        else:
                            sheet_current_result.cell(row=cell_current_source.row, column=cell_current_source.column,
                                                      value=hamming_codec_decode(str(cell_current_source.value)))
                    int_counter_done_operations += int_percentage_current_row_comlete / len(row_current_source)
                    print(int_counter_done_operations)
        file_source.close()
        file_result.remove(file_result['Sheet'])
        file_result.save(string_filepath_result)
