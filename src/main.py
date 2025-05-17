from textnode import *

def main():
    new_node = TextNode("Hello World", TextType.NORMAL, "http://example.com")
    print(new_node)
    return new_node



if __name__ == "__main__":
    main()