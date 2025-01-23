import sys
from enum import Enum
def func_wrapper():
    call_type = None
    file_full_path = None    
    class CALL_TYPE(Enum):
        ALL = 1
        LINES = 2
        WORDS = 3
        BYTES = 4
        CHARS = 5
        
    def handle_byte_count(line_bytes):
        return len(line_bytes)
        
    def handle_char_count(line_bytes):
        line_text = line_bytes.decode('utf-8')
        return len(line_text)
        
    def handle_word_count(line_bytes):
        line_text = line_bytes.decode('utf-8')
        return len(line_text.split())
       
    def get_file_name(full_path):
        splitted = full_path.split("\\")
        return splitted[len(splitted) - 1]

    def get_call_type(call_type_flag):
        if call_type_flag == '-l':
            return CALL_TYPE.LINES
        elif call_type_flag == '-w':
            return CALL_TYPE.WORDS
        elif call_type_flag == '-c':
            return CALL_TYPE.BYTES
        elif call_type_flag == '-m':
            return CALL_TYPE.CHARS
        else:
            return None
            
    def handle_cmd_params():
        nonlocal call_type
        nonlocal file_full_path
        if len(sys.argv) < 2:#cmd name only 
            #log('1')
            file_full_path = input()
            call_type = CALL_TYPE.ALL
        elif len(sys.argv) < 3:#also contains file name OR flag
            #log('2')
            if sys.argv[1].startswith('-'):#flag
                #log('2.1')
                file_full_path = input()
                call_type = get_call_type(sys.argv[1])        
            else:#file name
                #log('2.2')
                file_full_path = sys.argv[1]
                call_type = CALL_TYPE.ALL
        elif len(sys.argv) < 4:#also contains file name AND flag
            #log('3')
            file_full_path = sys.argv[2]
            call_type = get_call_type(sys.argv[1])
            
    def log(text):
        print(text)
       

    handle_cmd_params()
    if call_type == None:
        print(f"Invalid flag {sys.argv[1]}. must start with a hyphen and followed by one of [l,w,c,m]") 
        exit()
    line_count = 0
    word_count = 0
    char_count = 0
    byte_count = 0
    with open(file_full_path, 'br') as file:
        for line_bytes in file.readlines():
            if call_type == CALL_TYPE.ALL or call_type == CALL_TYPE.LINES:
                line_count += 1
            if call_type == CALL_TYPE.ALL or call_type == CALL_TYPE.WORDS:
                word_count += handle_word_count(line_bytes)
            if call_type == CALL_TYPE.ALL or call_type == CALL_TYPE.BYTES:          
                byte_count += handle_byte_count(line_bytes)
            if call_type == CALL_TYPE.CHARS:
                char_count += handle_char_count(line_bytes)
            
    line_count_str = str(line_count) + " " if call_type == CALL_TYPE.ALL or call_type == CALL_TYPE.LINES else ""
    word_count_str = str(word_count) + " " if call_type == CALL_TYPE.ALL or call_type == CALL_TYPE.WORDS else ""
    byte_count_str = str(byte_count) + " " if call_type == CALL_TYPE.ALL or call_type == CALL_TYPE.BYTES else ""
    char_count_str = str(char_count) + " " if call_type == CALL_TYPE.CHARS else ""
                
    print(f"    {line_count_str}{word_count_str}{char_count_str}{byte_count_str}{get_file_name(file_full_path)}")

func_wrapper()

    
