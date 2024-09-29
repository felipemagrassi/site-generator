from textnode import TextNode, TextType

def text_note_to_html_node(text_node):
    match text_node.text_type:
        case TextType.BOLD:
            pass




print(TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev"))
