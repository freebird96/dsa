"""
    Given an m x n board of characters and a list of strings words, return all words on the board
    Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.  

    Input: board = 
    [
        [ "o", "a", "a", "n" ],
        [ "e", "t", "a", "e" ],
        [ "i", "h", "k", "r" ],
        [ "i", "f", "l", "v" ]
    ]

    words = ["oath","pea","eat","rain"]
    Output: ["eat","oath", "bag", "bat", "big"]

"""
"""

    Things would have been easier if it were a Trie structure.
    meaning;
    {
        "b": {
            "a": {
                "t": {
                    "*": "bat"
                },
                "g": {
                    "*": "bag"
                }
            },
            "i": {
                "g": {
                    "*": "big"
                }
            }
        },
        "e": {
            "a": {
                "t": {
                    "*": "eat"
                }
            }
        },
        "o": {
            "a": {
                "t": {
                    "h": {
                        "*": "oath"
                    }
                }
            }
        }
    }


"""

# Time Complexity: O(n*m*4^L + w*L)
    # Time to traverse through the board and the words: O(nm*4^L)
    # Time to create the tree: O(w*L)

# Auxillary Space: O(n*m+wL)

# w = number of words
# L = Length of the longest word

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        # Step 1: construct a visted matrix to keep track of the items visited to avoid repeatition of letters.
        visited = [[False for letter in row] for row in board]
        final_words = {}
        # Step 2: Construct a Trie structure.
        trie = Trie()
        for word in words:
            trie.add_node(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.explore(i, j, board, visited, final_words, trie.node)
        
        return list(final_words.keys())


    def explore(self, i, j, board, visited, final_words, trie_node):
        """
            Look for all the letters and check if they are being present in the words
        """
        if visited[i][j]:
            return
        letter = board[i][j]
        if letter not in trie_node:
            return
        trie_node = trie_node[letter]
        visited[i][j] = True
        if '*' in trie_node:
            final_words[trie_node['*']] = True
        neighbors = self.get_neighbors(i, j, board)
        for neigh in neighbors:
            self.explore(neigh[0], neigh[1], board, visited, final_words, trie_node)
        visited[i][j] = False


    def get_neighbors(self, i, j, board):
        """
            Look for the neighbors & return the neighbors
        """
        neighs = []
        if i > 0:
            neighs.append([i-1, j])
        
        if j > 0:
            neighs.append([i, j-1])
        
        if i < len(board)-1:
            neighs.append([i+1, j])
        
        if j < len(board[0])-1:
            neighs.append([i, j+1])

        return neighs

class Trie:
    def __init__(self):
        self.node = {}
        self.end_symbol = "*"

    def add_node(self, word):
        current = self.node
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current[self.end_symbol] = word

board = [["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"],["b","a","b","a","b","a","b","a","b","a"],["a","b","a","b","a","b","a","b","a","b"]]
words =["aababababa","abbabababa","acbabababa","adbabababa","aebabababa","afbabababa","agbabababa","ahbabababa","aibabababa","ajbabababa","akbabababa","albabababa","ambabababa","anbabababa","aobabababa","apbabababa","aqbabababa","arbabababa","asbabababa","atbabababa","aubabababa","avbabababa","awbabababa","axbabababa","aybabababa","azbabababa","bababababa","bbbabababa","bcbabababa","bdbabababa","bebabababa","bfbabababa","bgbabababa","bhbabababa","bibabababa","bjbabababa","bkbabababa","blbabababa","bmbabababa","bnbabababa","bobabababa","bpbabababa","bqbabababa","brbabababa","bsbabababa","btbabababa","bubabababa","bvbabababa","bwbabababa","bxbabababa","bybabababa","bzbabababa","cababababa","cbbabababa","ccbabababa","cdbabababa","cebabababa","cfbabababa","cgbabababa","chbabababa","cibabababa","cjbabababa","ckbabababa","clbabababa","cmbabababa","cnbabababa","cobabababa","cpbabababa","cqbabababa","crbabababa","csbabababa","ctbabababa","cubabababa","cvbabababa","cwbabababa","cxbabababa","cybabababa","czbabababa","dababababa","dbbabababa","dcbabababa","ddbabababa","debabababa","dfbabababa","dgbabababa","dhbabababa","dibabababa","djbabababa","dkbabababa","dlbabababa","dmbabababa","dnbabababa","dobabababa","dpbabababa","dqbabababa","drbabababa","dsbabababa","dtbabababa","dubabababa","dvbabababa","dwbabababa","dxbabababa","dybabababa","dzbabababa","eababababa","ebbabababa","ecbabababa","edbabababa","eebabababa","efbabababa","egbabababa","ehbabababa","eibabababa","ejbabababa","ekbabababa","elbabababa","embabababa","enbabababa","eobabababa","epbabababa","eqbabababa","erbabababa","esbabababa","etbabababa","eubabababa","evbabababa","ewbabababa","exbabababa","eybabababa","ezbabababa","fababababa","fbbabababa","fcbabababa","fdbabababa","febabababa","ffbabababa","fgbabababa","fhbabababa","fibabababa","fjbabababa","fkbabababa","flbabababa","fmbabababa","fnbabababa","fobabababa","fpbabababa","fqbabababa","frbabababa","fsbabababa","ftbabababa","fubabababa","fvbabababa","fwbabababa","fxbabababa","fybabababa","fzbabababa","gababababa","gbbabababa","gcbabababa","gdbabababa","gebabababa","gfbabababa","ggbabababa","ghbabababa","gibabababa","gjbabababa","gkbabababa","glbabababa","gmbabababa","gnbabababa","gobabababa","gpbabababa","gqbabababa","grbabababa","gsbabababa","gtbabababa","gubabababa","gvbabababa","gwbabababa","gxbabababa","gybabababa","gzbabababa","hababababa","hbbabababa","hcbabababa","hdbabababa","hebabababa","hfbabababa","hgbabababa","hhbabababa","hibabababa","hjbabababa","hkbabababa","hlbabababa","hmbabababa","hnbabababa","hobabababa","hpbabababa","hqbabababa","hrbabababa","hsbabababa","htbabababa","hubabababa","hvbabababa","hwbabababa","hxbabababa","hybabababa","hzbabababa","iababababa","ibbabababa","icbabababa","idbabababa","iebabababa","ifbabababa","igbabababa","ihbabababa","iibabababa","ijbabababa","ikbabababa","ilbabababa","imbabababa","inbabababa","iobabababa","ipbabababa","iqbabababa","irbabababa","isbabababa","itbabababa","iubabababa","ivbabababa","iwbabababa","ixbabababa","iybabababa","izbabababa","jababababa","jbbabababa","jcbabababa","jdbabababa","jebabababa","jfbabababa","jgbabababa","jhbabababa","jibabababa","jjbabababa","jkbabababa","jlbabababa","jmbabababa","jnbabababa","jobabababa","jpbabababa","jqbabababa","jrbabababa","jsbabababa","jtbabababa","jubabababa","jvbabababa","jwbabababa","jxbabababa","jybabababa","jzbabababa","kababababa","kbbabababa","kcbabababa","kdbabababa","kebabababa","kfbabababa","kgbabababa","khbabababa","kibabababa","kjbabababa","kkbabababa","klbabababa","kmbabababa","knbabababa","kobabababa","kpbabababa","kqbabababa","krbabababa","ksbabababa","ktbabababa","kubabababa","kvbabababa","kwbabababa","kxbabababa","kybabababa","kzbabababa","lababababa","lbbabababa","lcbabababa","ldbabababa","lebabababa","lfbabababa","lgbabababa","lhbabababa","libabababa","ljbabababa","lkbabababa","llbabababa","lmbabababa","lnbabababa","lobabababa","lpbabababa","lqbabababa","lrbabababa","lsbabababa","ltbabababa","lubabababa","lvbabababa","lwbabababa","lxbabababa","lybabababa","lzbabababa","mababababa","mbbabababa","mcbabababa","mdbabababa","mebabababa","mfbabababa","mgbabababa","mhbabababa","mibabababa","mjbabababa","mkbabababa","mlbabababa","mmbabababa","mnbabababa","mobabababa","mpbabababa","mqbabababa","mrbabababa","msbabababa","mtbabababa","mubabababa","mvbabababa","mwbabababa","mxbabababa","mybabababa","mzbabababa","nababababa","nbbabababa","ncbabababa","ndbabababa","nebabababa","nfbabababa","ngbabababa","nhbabababa","nibabababa","njbabababa","nkbabababa","nlbabababa","nmbabababa","nnbabababa","nobabababa","npbabababa","nqbabababa","nrbabababa","nsbabababa","ntbabababa","nubabababa","nvbabababa","nwbabababa","nxbabababa","nybabababa","nzbabababa","oababababa","obbabababa","ocbabababa","odbabababa","oebabababa","ofbabababa","ogbabababa","ohbabababa","oibabababa","ojbabababa","okbabababa","olbabababa","ombabababa","onbabababa","oobabababa","opbabababa","oqbabababa","orbabababa","osbabababa","otbabababa","oubabababa","ovbabababa","owbabababa","oxbabababa","oybabababa","ozbabababa","pababababa","pbbabababa","pcbabababa","pdbabababa","pebabababa","pfbabababa","pgbabababa","phbabababa","pibabababa","pjbabababa","pkbabababa","plbabababa","pmbabababa","pnbabababa","pobabababa","ppbabababa","pqbabababa","prbabababa","psbabababa","ptbabababa","pubabababa","pvbabababa","pwbabababa","pxbabababa","pybabababa","pzbabababa","qababababa","qbbabababa","qcbabababa","qdbabababa","qebabababa","qfbabababa","qgbabababa","qhbabababa","qibabababa","qjbabababa","qkbabababa","qlbabababa","qmbabababa","qnbabababa","qobabababa","qpbabababa","qqbabababa","qrbabababa","qsbabababa","qtbabababa","qubabababa","qvbabababa","qwbabababa","qxbabababa","qybabababa","qzbabababa","rababababa","rbbabababa","rcbabababa","rdbabababa","rebabababa","rfbabababa","rgbabababa","rhbabababa","ribabababa","rjbabababa","rkbabababa","rlbabababa","rmbabababa","rnbabababa","robabababa","rpbabababa","rqbabababa","rrbabababa","rsbabababa","rtbabababa","rubabababa","rvbabababa","rwbabababa","rxbabababa","rybabababa","rzbabababa","sababababa","sbbabababa","scbabababa","sdbabababa","sebabababa","sfbabababa","sgbabababa","shbabababa","sibabababa","sjbabababa","skbabababa","slbabababa","smbabababa","snbabababa","sobabababa","spbabababa","sqbabababa","srbabababa","ssbabababa","stbabababa","subabababa","svbabababa","swbabababa","sxbabababa","sybabababa","szbabababa","tababababa","tbbabababa","tcbabababa","tdbabababa","tebabababa","tfbabababa","tgbabababa","thbabababa","tibabababa","tjbabababa","tkbabababa","tlbabababa","tmbabababa","tnbabababa","tobabababa","tpbabababa","tqbabababa","trbabababa","tsbabababa","ttbabababa","tubabababa","tvbabababa","twbabababa","txbabababa","tybabababa","tzbabababa","uababababa","ubbabababa","ucbabababa","udbabababa","uebabababa","ufbabababa","ugbabababa","uhbabababa","uibabababa","ujbabababa","ukbabababa","ulbabababa","umbabababa","unbabababa","uobabababa","upbabababa","uqbabababa","urbabababa","usbabababa","utbabababa","uubabababa","uvbabababa","uwbabababa","uxbabababa","uybabababa","uzbabababa","vababababa","vbbabababa","vcbabababa","vdbabababa","vebabababa","vfbabababa","vgbabababa","vhbabababa","vibabababa","vjbabababa","vkbabababa","vlbabababa","vmbabababa","vnbabababa","vobabababa","vpbabababa","vqbabababa","vrbabababa","vsbabababa","vtbabababa","vubabababa","vvbabababa","vwbabababa","vxbabababa","vybabababa","vzbabababa","wababababa","wbbabababa","wcbabababa","wdbabababa","webabababa","wfbabababa","wgbabababa","whbabababa","wibabababa","wjbabababa","wkbabababa","wlbabababa","wmbabababa","wnbabababa","wobabababa","wpbabababa","wqbabababa","wrbabababa","wsbabababa","wtbabababa","wubabababa","wvbabababa","wwbabababa","wxbabababa","wybabababa","wzbabababa","xababababa","xbbabababa","xcbabababa","xdbabababa","xebabababa","xfbabababa","xgbabababa","xhbabababa","xibabababa","xjbabababa","xkbabababa","xlbabababa","xmbabababa","xnbabababa","xobabababa","xpbabababa","xqbabababa","xrbabababa","xsbabababa","xtbabababa","xubabababa","xvbabababa","xwbabababa","xxbabababa","xybabababa","xzbabababa","yababababa","ybbabababa","ycbabababa","ydbabababa","yebabababa","yfbabababa","ygbabababa","yhbabababa","yibabababa","yjbabababa","ykbabababa","ylbabababa","ymbabababa","ynbabababa","yobabababa","ypbabababa","yqbabababa","yrbabababa","ysbabababa","ytbabababa","yubabababa","yvbabababa","ywbabababa","yxbabababa","yybabababa","yzbabababa","zababababa","zbbabababa","zcbabababa","zdbabababa","zebabababa","zfbabababa","zgbabababa","zhbabababa","zibabababa","zjbabababa","zkbabababa","zlbabababa","zmbabababa","znbabababa","zobabababa","zpbabababa","zqbabababa","zrbabababa","zsbabababa","ztbabababa","zubabababa","zvbabababa","zwbabababa","zxbabababa","zybabababa","zzbabababa"]
print(Solution().findWords(board, words))



