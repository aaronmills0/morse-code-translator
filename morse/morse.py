'''
    Morse code encoder and decoder

    'dot' is represented by '.'
    'dash' is represented by '-'
    character delimeter is ' '
    word delimeter is '/'


                                 ''
                    /                        \   
                 'e'                          't'
            /          \                  /          \ 
          'i'           'a'             'n'           'm'
        /     \       /     \         /     \       /     \ 
      's'     'u'   'r'      'w'    'd'      'k'  'g'      'o'
     /   \   /     /        /  \    /  \     / \  / \    
  'h'    'v''f'   'l'     'p'  'j''b'  'x' 'c' 'y''z''q'
            
'''

class Morse:

    class Node:
        def __init__(self, value, dot, dash):
            self.value = value
            self.dot = dot
            self.dash = dash
    def __init__(self):
        self.root = self.create_tree()
        self.mapping = {
            'a':'.-', 
            'b':'-...',
            'c':'-.-.',
            'd':'-..',
            'e':'.',
            'f':'..-.',
            'g':'--.',
            'h':'....',
            'i':'..',
            'j':'.---',
            'k':'-.-',
            'l':'.-..',
            'm':'--',
            'n':'-.',
            'o':'---',
            'p':'.--.',
            'q':'--.-',
            'r':'.-.',
            's':'...',
            't':'-',
            'u':'..-',
            'v':'...-',
            'w':'.--',
            'x':'-..-',
            'y':'-.--',
            'z':'--..',
            '0':'-----',
            '1':'.----',
            '2':'..---',
            '3':'...--',
            '4':'....-',
            '5':'.....',
            '6':'-....',
            '7':'--...',
            '8':'---..',
            '9':'....-',
            ',':'--..--',
            '?':'..--..',
            ':':'---...',
            '-':'-....-',
            '\"':'.-..-.',
            '(':'-.--.',
            '=':'-...-',
            '.':'.-.-.-',
            ';':'-.-.-.',
            '/':'-..-.',
            '\'':'.----.',
            '_':'..--.-',
            ')':'-.--.-',
            '+':'.--.-.',
            '@':'.--.-.',
            '&':'.-...',
            '!':'-.-.--'
            }
        self.n_p = {
            '-----':'0',
            '.----':'1',
            '..---':'2',
            '...--':'3',
            '....-':'4',
            '.....':'5',
            '-....':'6',
            '--...':'7',
            '---..':'8',
            '....-':'9',
            '--..--':',',
            '..--..':'?',
            '---...':':',
            '-....-':'-',
            '.-..-.':'\"',
            '-.--.':'(',
            '-...-':'=',
            '.-.-.-':'.',
            '-.-.-.':';',
            '-..-.':'/',
            '.----.':'\'',
            '..--.-':'_',
            '-.--.-':')',
            '.--.-.':'+',
            '.--.-.':'@',
            '.-...':'&',
            '-.-.--':'!'
        }
    def create_tree(self):
        root = self.Node('', None, None)
        root.dot = self.Node('e', None, None) # e: .
        root.dot.dot = self.Node('i', None, None) # i: ..
        root.dot.dash = self.Node('a', None, None) # a: .-
        root.dot.dot.dot = self.Node('s', None, None) # s: ...
        root.dot.dot.dash = self.Node('u', None, None) # u: ..-
        root.dot.dash.dot = self.Node('r', None, None) # r: .-.
        root.dot.dash.dash = self.Node('w', None, None) # w: .--
        root.dot.dot.dot.dot = self.Node('h', None, None) # h: ....
        root.dot.dot.dot.dash = self.Node('v', None, None) # v: ...-
        root.dot.dot.dash.dot = self.Node('f', None, None) # f: ..-.
        root.dot.dash.dot.dot = self.Node('l', None, None) # l: .-..
        root.dot.dash.dash.dot = self.Node('p', None, None) # p: .--.
        root.dot.dash.dash.dash = self.Node('j', None, None) # .---
        root.dash = self.Node('t', None, None) # t: -
        root.dash.dot = self.Node('n', None, None) # n: -.
        root.dash.dash = self.Node('m', None, None) # m: --
        root.dash.dot.dot = self.Node('d', None, None) # d: -..
        root.dash.dot.dash = self.Node('k', None, None) # k: -.-
        root.dash.dash.dot = self.Node('g', None, None) # g: --.
        root.dash.dash.dash = self.Node('o', None, None) # o: ---
        root.dash.dot.dot.dot = self.Node('b', None, None) # b: -...
        root.dash.dot.dot.dash = self.Node('x', None, None) # x: -..-
        root.dash.dash.dot.dot = self.Node('z', None, None) # z: --..
        root.dash.dash.dot.dash = self.Node('q', None, None) # q: --.-
        root.dash.dot.dash.dot = self.Node('c', None, None) # c: -.-.
        root.dash.dot.dash.dash = self.Node('y', None, None) # y: -.--
        return root
    
    def get_char(self, node, morse):
        if node is None:
            raise Exception
        if len(morse) == 0:
            return node.value
        elif morse[0] == '.':
            morse.pop(0)
            return self.get_char(node.dot, morse)
        else:
            morse.pop(0)
            return self.get_char(node.dash, morse)
    
    def encode(self, s):
        if s is None:
            print('Invalid string of characters.')
            return
        morse = ''
        chars = list(s.strip().lower())
        count = len(chars)
        while count > 0:
            cur = chars.pop(0)
            if (not(cur in self.mapping) and ord(cur) != 32):
                print('Invalid string of characters.')
                return
            if (ord(cur) == 32):
                morse += ' / '
            else:
                morse += self.mapping[cur]
                if count > 1:
                    morse += ' '
            count -= 1
        return morse
    
    def decode(self, morse):
        if morse is None:
            print("Invalid morse input.")
        s = ''
        arr = []
        words = morse.split('/')
        for word in words:
            word.strip()
            arr.append(word.split())
        for word in arr:
            for letter in word:
                if letter in self.n_p:
                    s += self.n_p[letter]
                else:
                    s += self.get_char(self.root, list(letter))
            s += ' '
        return s.strip()

        
    
if __name__ == '__main__':
    morse = Morse()
    while True:
        response = input('Enter \'e\' to encode an alphabetic string to a morse code string or a \'d\' to decode a morse code string to an alphabetic string.\n')
        response = response.lower()
        if response == 'e' or response == 'd':
            break
    
    if response == 'e':
        s = input('Enter the alphabetic string you would like to encode\n')
        print(morse.encode(s))
    else:
        m = input('Enter the morse code string you would like to decode\n')
        print(morse.decode(m))