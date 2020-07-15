import sys

class Node():
    def __init__(self, value, frequency = None):
        self.right = None
        self.left = None
        self.value = value
        self.frequency = frequency

class Huffman():
    def preprocess(self, data) -> list:
        dict = {}
        nodes = [];
        for char in data:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] = dict[char] + 1

        for key in dict:
            nodes.append(Node(key, dict[key]))

        return sorted(nodes, key=lambda x: x.frequency, reverse=True)

    def createTree(self, nodes) -> list:
        while (len(nodes) > 1):
            first = nodes.pop()
            second = nodes.pop()
            node = Node(None, first.frequency + second.frequency)
            node.left = first
            node.right = second
            nodes.append(node)
            nodes = sorted(nodes, key=lambda x: x.frequency, reverse=True)

        return nodes

    def convertTreeToBinary(self, node, data) -> list:
        dict = {}
        code = ''
        def getCode(node, currentCode=""):
            if (node.left == None and node.right == None):
                dict[node.value] = currentCode
            else:
                getCode(node.left, currentCode + "0")
                getCode(node.right, currentCode + "1")
        getCode(node)

        for char in data:
            code += dict[char]

        return code, node

    @staticmethod
    def encode(data = None):
        if data is None:
            raise ValueError('Value cannot be empty')

        data = str(data)
        if (len(data) > 0):
            huffman = Huffman()
            nodes = huffman.preprocess(data)
            tree = huffman.createTree(nodes)

            return huffman.convertTreeToBinary(tree[0], data)

        raise ValueError('Value cannot be empty')

    @staticmethod
    def decode(huffman, tree):
        if (len(huffman) > 0):
            original = ''
            node = tree
            for char in huffman:
                if (int(char) == 0):
                    node = node.left
                else:
                    node = node.right

                if (node.value is not None):
                    original += node.value
                    node = tree
        else:
            original = ''
            for i in range(tree.frequency):
                original += tree.value

        return original

if __name__ == "__main__":
    try:
        a_great_sentence = "The bird is the word"

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = Huffman.encode(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = Huffman.decode(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))

        assert decoded_data == a_great_sentence

        a_great_sentence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV"

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = Huffman.encode(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = Huffman.decode(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))

        assert decoded_data == a_great_sentence

        a_great_sentence = "aaaa"

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = Huffman.encode(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = Huffman.decode(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))

        assert decoded_data == a_great_sentence

        a_great_sentence = ""

        print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
        print ("The content of the data is: {}\n".format(a_great_sentence))

        encoded_data, tree = Huffman.encode(a_great_sentence)

        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = Huffman.decode(encoded_data, tree)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the decoded data is: {}\n".format(decoded_data))

        assert decoded_data == a_great_sentence
    except ValueError as e:
        print(e)