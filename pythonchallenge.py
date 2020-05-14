from PIL import Image
import xmlrpc.client
import itertools
from requests.auth import HTTPBasicAuth
import bz2
from PIL import Image, ImageDraw
import zipfile
import shutil
import pickle
import requests
import re
import string
import os

os.chdir('/Users/ilja/Dropbox/challenges')

print("-------------------- 1 TRANSLATION --------------------")
# list_of_dicts = []
# for n in range(26):
#     dict = {}
#     correct = list(string.ascii_lowercase)
#     shifted = list(string.ascii_lowercase)
#
#     for i in range(n):
#         p = list(shifted.pop())
#         p.extend(shifted)
#         shifted = p
#
#     for c, s in zip(correct, shifted):
#         dict.update({
#             c: s
#         })
#
#     list_of_dicts.append(dict)
#
#     # print(n, dict['a'])
#
# for i, dict in enumerate(list_of_dicts):
#
#     seq = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
#
#     decoded = []
#     for letter in seq:
#         # the second argument is there to ensure that if it can't procure a letter in the dict it use the existing one
#         decoded.append(dict.get(letter, letter))
#     decoded_s = ''.join(decoded)
#     # print(decoded_s)
#
# """
# i hope you didnt translate it by hand.
# thats what computers are for.
# doing it in by hand is inefficient and that's why this text is so long.
# using string.maketrans() is recommended. now apply on the url.
# """

# ==============================================================================
# simpler way
# dict = {}
# correct = list(string.ascii_lowercase)
# shifted = list(string.ascii_lowercase)
#
# for i in range(24):  # 24 = 2 back. Initially I tried 2 fwd and hence failed
#     p = list(shifted.pop())
#     p.extend(shifted)
#     shifted = p
#
# correctString = ''.join(correct)
# shiftedString = ''.join(shifted)
# # print(shiftedString)
#
# thirdString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
# urlString = "pc/def/map.html"
# tt = str.maketrans(correctString, shiftedString)
# ttt = urlString.translate(tt)
# print(ttt)

# ==============================================================================
# s1 = 'abc'
# s2 = 'def'
# s3 = 'abczz'
# dict = str.maketrans(s1, s2)
# print(s3.translate(dict))  # defzz

print("-------------------- 2 OCR CHALLENGE --------------------")
# with open('rare_chars.txt') as f:
#     txt = f.read()
#
#     # doesn't work because it returns an arbitary ordered string and I can't read it
#     # stxt = set(txt)
#
#     # manual method
#     # short = ''
#     # unique = []
#     # for i in txt:
#     #     if i not in unique:
#     #         unique.append(i)
#     # print(unique)
#     #
#     # for i in unique:
#     #     cnt = txt.count(i)
#     #     if cnt < 2:
#     #         short += i
#     # print(short)
#
#     # their method
#     occurences = {}
#     for c in txt:
#         # very nice we're getting and setting at the same time
#         occurences[c] = occurences.get(c, 0)+1
#
#     avgOc = len(txt)//len(occurences)
#     print(''.join([c for c in occurences if occurences[c] < avgOc]))


print("-------------------- 3 SMALL TEXT --------------------")
# r = re.compile(r'[^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]')
#
# with open('small_letter.txt') as f:
#     txt = f.read()
#     mo = r.findall(txt)
#     print(mo)

print("-------------------- 4 NEXT NOTHING --------------------")

# res = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=45439')

# r = re.compile(r'(\d)*$')
# while True:
#     r = re.compile(r'by two')
#     try:
#         mo = r.search(res.text)
#         ans = mo.group()
#
#         # then...
#         break
#     except:
#         r = re.compile(r'(\d)*$')
#         mo = r.search(res.text)
#         ans = mo.group()
#         print(res.text)
#         res = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={ans}')
#
# # when we break out of the first loop we start the second loop
# while True:
#     r = re.compile(r'(\d)*$')
#     mo = r.search(res.text)
#     print(res.text)
#     ans = int(mo.group())
#     print(ans)
#     ans = ans//2
#     print(res.text)
#     res = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={ans}')


# r = re.compile(r'(\d)*$')
# while True:
#     print(res.text)
#     if 'Divide by two' in res.text:
#         print(ans)
#         ans = int(ans)//2
#         res = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={ans}')
#     else:
#         r = re.compile(r'(\d)*$')
#         mo = r.search(res.text)
#         ans = mo.group()
#         res = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={ans}')


print("-------------------- 5 PEAK HELL --------------------")

# # get the text
# res = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
# res.raise_for_status()
#
# # first encode so that it becomes a bytes object
# # next load into a pickle - note we're using loadS for string
# p = pickle.loads(res.text.encode())
#
# # what comes back is a compression algorithm - character vs number of appearances
# print(p)
#
# # let's unpack it into a file
# with open('hidden_text2.txt', 'w') as f:
#
#     for line in p:
#         print(line)
#         l = ''
#         for tup in line:
#             print(tup[0])
#             print(tup[1])
#             l += str(tup[0])*int(tup[1])
#         l += '\n'
#         f.write(l)
#
# # a nicer way to do it
# for line in p:
#     print("".join(
#         # map is a nice replacement for a loop - we repetively apply some function to every element in the array
#         map(lambda pair: pair[0]*pair[1], line)
#
#         # an even nicer way to do it - use a generator function and unpack tuples right inside of it
#         (ch * count for ch, count in line)
#     ))

print("-------------------- 6 UNZIP --------------------")
# res = requests.get('http://www.pythonchallenge.com/pc/def/channel.zip')
# res.raise_for_status()
# with open('channel2.zip', 'wb') as f:
#     for chunk in res.iter_content(100_000): #yes you MUST chunk or it doesn't save correctly
#         f.write(chunk)

# MY APPROACH - BUT CAN'T EXTRACT COMMENTS
# docs = [f for f in os.listdir('channel2')]
# print(docs)
# r = re.compile(r'(\d)+$')
# doc = docs[0]
# while True:
#     with open('channel2/'+doc) as f:
#         txt = f.read()
#         print(txt)
#         mo = r.search(txt)
#         doc = mo.group()+'.txt'

# THEIR APPROACH -
# r = re.compile(r'(\d)+$')
# doc = '90052.txt'  # this was in the html file and I missed it
#
# with zipfile.ZipFile('channel2.zip') as myzip:
#     comments = []
#     while True:
#         with myzip.open(doc) as myfile:
#             txt = myfile.read().decode()
#             c = myzip.getinfo(doc).comment.decode()
#             comments.append(c)
#             # print(c)
#             print(txt)
#
#             try:
#                 mo = r.search(txt)
#                 doc = mo.group()+'.txt'
#             except:
#                 break
#
# print("".join(comments))

print("-------------------- 7 OXYGEN --------------------")
# nothing interesting except for the image
# res = requests.get("http://www.pythonchallenge.com/pc/def/oxygen.html")
# res.raise_for_status()
# print(res.text)
#
# lets get the image
# res = requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png")
# res.raise_for_status()
# with open('oxyge.png', 'wb') as f:
#     for chunk in res.iter_content(100_000):
#         f.write(chunk)

# img = Image.open('oxygen.png')
# # we want the pixels from the middle row
# w, h = img.size
#
# # get row of pixels
# row = [img.getpixel((x, h//2+1)) for x in range(w)]
# # strip non-gray ones
# row = [r for r, g, b, a in row if r == g == b]
# # strip duplicates (We know each one is 7 pixels wide so take each 7th only)
# row = row[::7]
# # convert to ascii
# # txt = ''.join([chr(x) for x in row])
# txt = ''.join(map(chr, row))  # ALTERNATIVE - USE THER MAP FUNCTION
# # extract the numbers
# r = re.compile(r'\d+')
# mo = r.findall(txt)
# # decode into letters
# answer = "".join([chr(int(m)) for m in mo])
# print(answer)

print("-------------------- 8 INTEGRITY --------------------")
# res = requests.get("http://www.pythonchallenge.com/pc/def/integrity.html")
# print(res.text)
#
# un = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
# pw = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
#
# # ok so above is NOT a string to be converted into ascii - it's a specific format called bz, which we could have identified based on "BZ..."
# un = bz2.decompress(un)
# pw = bz2.decompress(pw)
# print(un, pw)

print("-------------------- 9 HUGE FILE --------------------")
# res = requests.get('http://www.pythonchallenge.com/pc/return/good.html',
# auth = HTTPBasicAuth('huge', 'file'))
# print(res.text)

first = """
146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,170,329,170,320,170,
310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,194,296,195,305,194,307,191,312,190,316,
190,321,192,331,193,338,196,341,197,346,199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,
389,191,392,190,396,189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,215,306,216,296,218,
290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,261,293,265,291,271,291,273,289,278,287,
279,285,281,280,284,278,284,276,287,277,289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,
327,306,332,307,341,306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,343,269,344,262,346,
259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,349,298,354,293,356,286,354,279,352,268,
352,257,351,249,350,234,351,211,352,197,354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,
120,314,116,304,117,293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,170,125,176,114,176,
102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,136,115,129,115,124,115,120,115,115,117,
113,120,109,122,102,122,100,121,95,121,89,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,
133,110,136,107,138,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161,
111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276,143,290,148,310,151,
332,155,348,156,353,153,366,149,379,147,394,146,399
"""

second = """
156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,168,157,163,157,159,
157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,152,212,147,215,146,218,143,220,132,220,
125,217,119,209,116,196,115,185,114,172,114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,
77,155,81,148,87,140,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
158,121,157,128,156,134,157,136,156,136
"""

# first = [int(i.strip('\n')) for i in first.split(',')]
# second = [int(i.strip('\n')) for i in second.split(',')]
# print(first)
#
# # I thought maybe I had to convert to tuples to fix: SystemError: new style getargs format but argument is not a tuple? - but turns out the real problem is, bu turns out the problem was the numbers INSIDE the tuple were casted as strings not as tuples
# # first = list(zip(first, first[1:]))
# # first = [f for i, f in enumerate(first) if i % 2 == 0]
# # print(type(first[0][0]))
#
#
# im = Image.new('RGB', (500, 500))
# draw = ImageDraw.Draw(im)
# draw.polygon(first, fill='white')
# draw.polygon(second, fill='orange')
# im.save('cow.png')

print("-------------------- 10 COW --------------------")
# so we need an algo for look and say sequence

# this approach fails because it will add up all the ones at the back and upfront
# seq = '1'
# ss = []
# for i in range(10):
#     dict = {}
#     print(f'gonna analyze... {seq}')
#     for s in seq:
#         dict[s] = dict.get(s, 0)+1
#     print(dict)
#     # dict to LoL
#     new_seq = [(value, key) for key, value in list(dict.items())]
#     # print(f"about to flatten.. {new_seq}")
#     # flatten LoL
#     new_seq = list(itertools.chain.from_iterable(new_seq))
#     # print(f"about to convert to string.. {new_seq}")
#     # to string
#     new_seq = [str(i) for i in new_seq]
#     new_seq = "".join(new_seq)
#     ss.append(new_seq)
#     seq = new_seq
#
# print(ss)

# works beautifully
# seq = [1]
# sequences = {}
# for i in range(1, 35):
#     g = itertools.groupby(seq)
#     seq = []
#     for key, grp in g:
#         grp = list(grp)
#         seq.append(len(grp))
#         seq.append(key)
#     sequences[i] = len(seq)
# print(sequences)

print("-------------------- 11 5808 --------------------")
# res = requests.get('http://www.pythonchallenge.com/pc/return/cave.jpg',
#                    auth=HTTPBasicAuth('huge', 'file'))
# res.raise_for_status()
# with open('cave.jpg', 'wb') as f:
#     for chunk in res.iter_content(100_000):
#         f.write(chunk)

# im = Image.open('cave.jpg')
# w, h = im.size
#
# even = Image.new('RGB', (w//2, h//2))
# odd = Image.new('RGB', (w//2, h//2))
#
# for i in range(w):
#     for j in range(h):
#         p = im.getpixel((i, j))
#         if (i+j) % 2 == 1:
#             odd.putpixel((i//2, j//2), p)
#         else:
#             even.putpixel((i//2, j//2), p)
#
# even.save('even.jpg')
# odd.save('odd.jpg')

print("-------------------- 12 EVIL --------------------")

# first we get this weird thing in gfx format
# res = requests.get('http://www.pythonchallenge.com/pc/return/evil2.gfx',
#                    auth=HTTPBasicAuth('huge', 'file'))
# res.raise_for_status()
# with open('evil.gfx', 'wb') as f:
#     for chunk in res.iter_content(100_000):
#         f.write(chunk)

# then we convert it to 5 images (split into 5 hands)
# with open('evil.gfx', 'rb') as f:
#     txt = f.read()
#     print(txt)
#     for i in range(5):
#         open('%d.jpg' % i, 'wb').write(txt[i::5])

print("-------------------- 13 DISPROPORTIONAL --------------------")

# this time we have to work with xml
# conn = xmlrpc.client.ServerProxy('http://www.pythonchallenge.com/pc/phonebook.php')
# print(conn.phone('Bert'))

print("-------------------- 14 ITALY --------------------")
# res = requests.get("http://www.pythonchallenge.com/pc/return/wire.png",
#                    auth=HTTPBasicAuth('huge', 'file'))
# res.raise_for_status()
# with open('wire.png', 'wb') as f:
#     for chunk in res.iter_content(100_000):
#         f.write(chunk)

im = Image.open("wire.png")
print(im.size)
