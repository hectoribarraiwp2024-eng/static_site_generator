from enum import Enum

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def markdown_to_blocks(markdown):
    split_markdown = markdown.split('\n\n')
    block_list = []
    for line in split_markdown:
        if line != '':
            block_list.append(line.strip())
    return block_list

def block_to_block_type(text):
    headings = ['# ', '## ', '### ', '#### ', '##### ', '###### ']
    for heading in headings:
        if heading in text:
            return BlockType.HEADING
        
    code_check = text.split('\n')
    if '```' == code_check[0] and '```' == code_check[-1]:
        return BlockType.CODE
    
    quote_check = text.split('\n')
    count = 1
    for line in quote_check:
        if line[0] != '>':
            count = 0
    if count == 1:
        return BlockType.QUOTE
    
    unordered_check = text.split('\n')
    count = 1
    for line in unordered_check:
        if line[0:2] != '- ':
            count = 0
    if count == 1:
        return BlockType.UNORDERED_LIST
    
    ordered_check = text.split('\n')
    count = 1
    check = 1
    for line in ordered_check:
        if not line.startswith(f"{count}. "):
            check = 0
        count += 1
    if check == 1:
        return BlockType.ORDERED_LIST
    
    return BlockType.PARAGRAPH
    