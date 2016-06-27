"""

Based of of this LeetSpeek generator:
https://github.com/floft/leetspeak/blob/master/LeetSpeak.py
"""
class Leet:
    def __init__(self, word=None):
        if word is None:
            raise exception('No word provided')
        self.word = word

        self.a=['a','4']
        self.b=['b','8','6']
        self.c=['c','k']
        self.d=['d','0']
        self.e=['e','3']
        self.f=['f']
        self.g=['g','6','9']
        self.h=['h']
        self.i=['i','!','1','|','l']
        self.j=['j']
        self.k=['k','x']
        self.l=['l','1','7']
        self.m=['m','nn']
        self.n=['n']
        self.o=['o','0']
        self.p=['p','9','q']
        self.q=['q','9']
        self.r=['r']
        self.s=['s','5','z','es','2']
        self.t=['t','7','1']
        self.u=['u','m']
        self.v=['v']
        self.w=['w','vv']
        self.x=['x','ex']
        self.y=['y','j']
        self.z=['z','2']
        self.zero=['0','o']
        self.one=['1','l']
        self.two=['two','2','z']
        self.three=['e','3','three']
        self.four=['4','four','for','fore','a']
        self.five=['5','five','s']
        self.six=['6','six','g']
        self.seven=['7','seven','t','l']
        self.eight=['8','eight','b']
        self.nine=['9','nine','g']
        
        self.alphabet={ 'a':self.a, 'b':self.b, 'c':self.c, 
                'd':self.d, 'e':self.e, 'f':self.f, 'g':self.g, 
                'h':self.h, 'i':self.i, 'j':self.j, 'k':self.k, 
                'l':self.l, 'm':self.m, 'n':self.n, 'o':self.o, 
                'p':self.p, 'q':self.q, 'r':self.r, 's':self.s, 
                't':self.t, 'u':self.u, 'v':self.v, 'w':self.w, 
                'x':self.x, 'y':self.y, 'z':self.z, '0':self.zero,
                '1':self.one,'2':self.two,'3':self.three,'4':self.four,
                '5':self.five,'6':self.six,'7':self.seven,'8':self.eight,
                '9':self.nine }

    def get_permutations(self, letter):
        try:
            permutations = self.alphabet[letter]
        except KeyError:
            permutations = letter
        regex = '['
        for p in permutations[:-1]:
            regex += '{0}|'.format(p)
        regex += '{0}]'.format(permutations[-1])

        return regex

    def get_regex(self):
        result = ''
        for letter in self.word:
            result += self.get_permutations(letter) 
        return result

    def get_regex_duplicate(self):
        result = ''
        length = len(self.word)
        duplicate = False 
        for i in range(length):
            if i == 0:
                result += self.get_permutations(self.word[i])
            elif self.word[i] == self.word[i-1] and not duplicate:
                duplicate = True
                result += '+'
            elif self.word[i] != self.word[i-1]:
                duplicate = False
                result += self.get_permutations(self.word[i])
        return result
