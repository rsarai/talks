from __future__ import division
import sys

class PythonBrasil:

    def __init__(self, v0, v1, v2, v3, v4):
        self.pybr19 = v0
        self.pybr18 = v1
        self.pybr17 = v2
        self.pybr16 = v3
        self.pybr15 = v4

    def __repr__(self):
        return 'PythonBrasil(%r, %r, %r, %r, %r)' % (
            self.pybr19, self.pybr18, self.pybr17, self.pybr16, self.pybr15
        )


places = PythonBrasil('ribeirão preto', 'natal', 'belo horizonte', 'florianopolis', 'sao jose dos campos')
vars(places)
# {'pybr19': 'ribeirão preto',
#  'pybr18': 'natal',
#  'pybr17': 'belo horizonte',
#  'pybr16': 'florianopolis',
#  'pybr15': 'sao jose dos campos'}
print(list(map(sys.getsizeof, map(vars, [places]))))


keys = ['pybr19', 'pybr18', 'pybr17', 'pybr16', 'pybr15', 'pybr14', 'pybr13']
values = [
    'ribeirão preto', 'natal', 'belo horizonte', 
    'florianopolis', 'sao jose dos campos', 'recife', 
    'brasilia'
]
hashes = list(map(abs, map(hash, keys)))
entries = list(zip(hashes, keys, values))

### default hashes for the talk
[(6519378555130876693, 'pybr19', 'ribeirão preto'),
 (1831110896825541078, 'pybr18', 'natal'),
 (9167591958126575224, 'pybr17', 'belo horizonte'),
 (4819543372031726241, 'pybr16', 'florianopolis'),
 (5067670214198873854, 'pybr15', 'sao jose dos campos'),
 (2940889712379195968, 'pybr14', 'recife'),
 (8949678210916869228, 'pybr13', 'brasilia')]


# [(664345387291340802, 'pybr19', 'ribeirão preto'),
#  (1193475843086917206, 'pybr18', 'natal'),
#  (2115422158974348649, 'pybr17', 'belo horizonte'),
#  (892364505439629757, 'pybr16', 'florianopolis'),
#  (2020306873403470778, 'pybr15', 'sao jose dos campos')]


def bits(n):
    n += 2**32
    return bin(n)[-32:]


def get_size(d):
    import sys
    return list(map(sys.getsizeof, map(vars, [d])))

d = dict()
d['pybr19'] = 'ribeirão preto'
bits(hash('pybr19'))[-3:]
'101'

"""
 -------------------------------------------------------
|  Idx      hash            key             value       |
 -------------------------------------------------------
|  000   |             |           |                    |
|  001   |             |           |                    |
|  010   |             |           |                    |
|  011   |             |           |                    |
|  100   |             |           |                    |
|  101   |  _00010101  |  pybr19   |  ribeirão preto    |
|  110   |             |           |                    |
|  111   |             |           |                    |
 -------------------------------------------------------
"""

d['pybr18'] = 'natal'
bits(hash('pybr18'))[-3:]
'110'

"""
 -------------------------------------------------------
|  Idx      hash            key             value       |
 -------------------------------------------------------
|  000   |             |           |                    |
|  001   |             |           |                    |
|  010   |             |           |                    |
|  011   |             |           |                    |
|  100   |             |           |                    |
|  101   |  _00010101  |  pybr19   |  ribeirão preto    |
|  110   |  _11010110  |  pybr18   |       natal        |
|  111   |             |           |                    |
 -------------------------------------------------------
"""

d['pybr17'] = 'belo horizonte'
bits(hash('pybr17'))[-3:]
'000'

"""
 -------------------------------------------------------
|  Idx      hash            key             value       |
 -------------------------------------------------------
|  000   |  _01111000  |  pybr17   |   belo horizonte   |
|  001   |             |           |                    |
|  010   |             |           |                    |
|  011   |             |           |                    |
|  100   |             |           |                    |
|  101   |  _00010101  |  pybr19   |  ribeirão preto    |
|  110   |  _11010110  |  pybr18   |       natal        |
|  111   |             |           |                    |
 -------------------------------------------------------
"""

d['pybr16'] = 'florianopolis'
bits(hash('pybr16'))[-3:]
'001'

"""
 -------------------------------------------------------
|  Idx      hash            key             value       |
 -------------------------------------------------------
|  000   |  _01111000  |  pybr17   |   belo horizonte   |
|  001   |  _10100001  |  pybr16   |   florianopolis    |
|  010   |             |           |                    |
|  011   |             |           |                    |
|  100   |             |           |                    |
|  101   |  _00010101  |  pybr19   |  ribeirão preto    |
|  110   |  _11010110  |  pybr18   |       natal        |
|  111   |             |           |                    |
 -------------------------------------------------------
"""

d['pybr15'] = 'sao jose dos campos'
bits(hash('pybr15'))[-3:]
'110'

"""
 -------------------------------------------------------
|  Idx      hash            key             value       |
 -------------------------------------------------------
|  000   |  _01111000  |  pybr17   |   belo horizonte   |
|  001   |  _10100001  |  pybr16   |   florianopolis    |
|  010   |             |           |                    |
|  011   |             |           |                    |
|  100   |             |           |                    |
|  101   |  _00010101  |  pybr19   |  ribeirão preto    |
|  110   |  _11010110  |  pybr18   |       natal        |
|  111   |             |           |                    |
 -------------------------------------------------------
"""

# open_addressing_multihash
"""
 -------------------------------------------------------
|  Idx      hash            key             value       |
 -------------------------------------------------------
|  000   |  _01111000  |  pybr17   |   belo horizonte   |
|  001   |  _10100001  |  pybr16   |   florianopolis    |
|  010   |             |           |                    |
|  011   |  _11111110  |  pybr15   | sao jose dos campos|
|  100   |             |           |                    |
|  101   |  _00010101  |  pybr19   |  ribeirão preto    |
|  110   |  _11010110  |  pybr18   |       natal        |
|  111   |             |           |                    |
 -------------------------------------------------------
"""

import sys
d = dict()
sys.getsizeof(d)

d['pybr19'] = 'ribeirão preto'
d['pybr18'] = 'natal'
d['pybr17'] = 'belo horizonte'
d['pybr16'] = 'florianopolis'
d['pybr15'] = 'sao jose dos campos'
sys.getsizeof(d)

d['pybr14'] = 'recife'
sys.getsizeof(d)





def print_table(result, entries):
    print("-------------------------------------------------------")
    print("|  Idx      hash            key             value       |")
    print("-------------------------------------------------------")
    for i, row in enumerate(result):
        if row:
            print(f"|  {bits(entries[i][0])[-5:]}  |  _{bits(entries[i][0])[-8:]}  |  {row[0]}  |  {row[1]}  |")
        else:
            print("empty")



















In [1]: d = {}
In [2]: d['pybr18'] = 'natal'
In [3]: bits(hash('pybr18'))[-3:]
Out[4]: '001'

"""
 -------------------------------------------------------
|  Idx      hash            key             value       |
 -------------------------------------------------------
|  000   |             |           |                    |
|  010   |             |           |                    |
|  001   | _11100001   |  pybr18   |  natal             |
|  011   |             |           |                    |
|  100   |             |           |                    |
|  101   |             |           |                    |
|  110   | _00101110   |  pybr19   |  ribeirão preto    |
|  111   |             |           |                    |
 -------------------------------------------------------
"""


def compact_and_ordered(n, entries):
    import pprint
    table = [None] * n
    for pos, entry in enumerate(entries):
        h = perturb = entry[0]
        i = h % n
        while table[i] is not None:
            i = (5 * i + perturb + 1) % n
            perturb >>= 5
        table[i] = pos
    pprint.pprint(entries)
    pprint.pprint(table)


def compact_and_ordered(n, entries):
    import pprint
    table = [None] * n
    for pos, entry in enumerate(entries):
        h = perturb = entry[0]
        i = h % n
        while table[i] is not None:
            i = (5 * i + perturb + 1) % n
            perturb >>= 5
        table[i] = pos
    pprint.pprint(entries)
    return table


def open_addressing_multihash(n, entries):
    table = [None] * n
    for h, key, value in entries:
        perturb = h
        i = h % n
        while table[i] is not None:
            print('%r collided with %r' % (key, table[i][0]))
            i = (5 * i + perturb + 1) % n
            perturb >>= 5
        table[i] = (key, value)
    print(table)


def open_addressing_multihash(n, entries):
    table = [None] * n
    for h, key, value in entries:
        perturb = h
        i = h % n
        while table[i] is not None:
            print('%r collided with %r' % (key, table[i][1]))
            i = (5 * i + perturb + 1) % n
            perturb >>= 5
        table[i] = (bits(h)[-3:], key, value)
    print(table)


def open_addressing_multihash(n, entries):
    table = [None] * n
    for h, key, value in entries:
        perturb = h
        i = h % n
        while table[i] is not None:
            print('%r collided with %r' % (key, table[i][1]))
            i = (5 * i + perturb + 1) % n
            perturb >>= 5
        table[i] = (bits(h)[-5:], key, value)
    print(table)




"""
 -------------------------------------------------------
|  idx   |    hash     |   key     |        value       |
 -------------------------------------------------------
|  000   |             |           |                    |
|  001   |             |           |                    |
|  010   |             |           |                    |
|  011   |             |           |                    |
|  100   |             |           |                    |
|  101   |             |           |                    |
|  110   |             |           |                    |
|  111   |             |           |                    |
 -------------------------------------------------------
"""

"""
 -------------------------------------------------------
|  idx   |    hash     |   key     |        value       |
 -------------------------------------------------------
|  000   |             |           |                    |
|  001   |             |           |                    |
|  010   |             |           |                    |
|  011   |             |           |                    |
|  100   |             |           |                    |
|  101   |             |           |                    |
|  110   |  _00101110  |   pybr19  |  ribeirão preto    |
|  111   |             |           |                    |
 -------------------------------------------------------
"""


"""
 -------------------------------------------------------
|  idx   |    hash     |   key     |        value       |
 -------------------------------------------------------
|  000   |             |           |                    |
|  001   |  _11100001  |   pybr18  |       natal        |
|  010   |             |           |                    |
|  011   |             |           |                    |
|  100   |             |           |                    |
|  101   |             |           |                    |
|  110   |  _00101110  |   pybr19  |  ribeirão preto    |
|  111   |             |           |                    |
 -------------------------------------------------------
"""

"""
 -------------------------------------------------------
|  idx   |    hash     |   key     |      value         |
 -------------------------------------------------------
|  000   |             |           |                    |
|  001   | _11100001   |  pybr18   |  natal             |
|  010   |             |           |                    |
|  011   | _11110011   |  pybr17   |  belo horizonte    |
|  100   |             |           |                    |
|  101   |             |           |                    |
|  110   | _00101110   |  pybr19   |  ribeirão preto    |
|  111   |             |           |                    |
 -------------------------------------------------------
"""

"""
 -------------------------------------------------------
|  idx   |    hash     |   key     |      value         |
 -------------------------------------------------------
|  000   |    '--'     |   '--'    |       '--'         |
|  001   | _11100001   |  pybr18   |  natal             |
|  010   |    '--'     |   '--'    |       '--'         |
|  011   | _11110011   |  pybr17   |  belo horizonte    |
|  100   |    '--'     |   '--'    |       '--'         |
|  101   | _01001110   |  pybr16   |  florianopolis     |
|  110   | _00101110   |  pybr19   |  ribeirão preto    |
|  111   |    '--'     |   '--'    |       '--'         |
 -------------------------------------------------------
"""

"""
 -------------------------------------------------------
|  idx   |    hash     |   key     |      value         |
 -------------------------------------------------------
|  000   |    '--'     |   '--'    |       '--'         |
|  001   | _11100001   |  pybr18   |  natal             |
|  010   |    '--'     |   '--'    |       '--'         |
|  011   | _11110011   |  pybr17   |  belo horizonte    |
|  100   |    '--'     |   '--'    |       '--'         |
|  101   |    '--'     |   '--'    |       '--'         |
|  110   | _00101110   |  pybr19   |  ribeirão preto    |
|  111   |    '--'     |   '--'    |       '--'         |
 -------------------------------------------------------
 """
