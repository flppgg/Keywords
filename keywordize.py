import nltk, Levenshtein, datetime, chardet, ast
from nltk.corpus import words
path='c:\users\carla\desktop\\'
bunch=1000

list_of_articles=[]
good_candidates=frozenset(['NN','NNS','NNP','NNPS','JJ','VBN'])
#structure of list_of_articles = [['title1',['seq-of-3'],['seq-of-2'],['approved-of-3'],['approved-of-2']],['title2',..]]

insieme=frozenset(words.words())

ora=datetime.datetime.now()
print 'opening file '+str(ora)
with open(path+'madonna.txt','r') as f:
    u=[]
    for l in f:
        #u.append(ast.literal_eval(l))
        #print l
        #encoding=chardet.detect(l)['encoding']
        #print encoding
        try:
             u.append(l.decode('windows-1252').lower())
        except:
            continue
        if len(u)==bunch+1000:
            break
        
                 
orapiu=datetime.datetime.now()
print 'cleaning file of scum '+str(orapiu-ora)
y=1

for line in u:
    a=[]
    if '???' not in line:
        tokenss=nltk.word_tokenize(line)
        if len(tokenss) >= 4:
            if tokenss[0] not in insieme:
                if tokenss[1] not in insieme:
                    if tokenss[2] not in insieme:
                        if tokenss[3] not in insieme:
                            y+=1
                            continue
            a.append(unicode.strip(line,'\n'))
            list_of_articles.append(a)
        else:
            y+=1
    else:
        y+=1
orapiu=datetime.datetime.now()
print str(y)+' titles rejected '+str(orapiu-ora)

for a in list_of_articles:
    if len(a) == 1:
        a.append([])
        a.append([])
        a.append([])
        a.append([])
    elif len(a) == 2:
        a.append([])
        a.append([])
        a.append([])
    elif len(a) == 3:
        a.append([])
        a.append([])
    elif len(a) == 4:
        a.append([])

orapiu=datetime.datetime.now()
print 'all lists are ready. Finding Candidates... '+str(orapiu-ora)

def keywordize(list_of_articles):
    for article in list_of_articles:
        tokens=nltk.word_tokenize(article[0])
        tagged=nltk.pos_tag(tokens)
        y=list(enumerate(tagged))
        
        for i in y:
            if i[1][1] in good_candidates:
                try:
                    n=y[i[0]+1]
                except IndexError:
                    break
                if n[1][1] in good_candidates:
                    try:
                        m = y[i[0]+2]
                    except IndexError:
                        article[2].append(i[1][0]+' '+n[1][0])
                        break
                    if m[1][1] in good_candidates:
                        article[1].append(i[1][0]+' '+n[1][0]+' '+m[1][0])
                        article[2].append(i[1][0]+' '+n[1][0])
                    else:
                        article[2].append(i[1][0]+' '+n[1][0])
                        

##import cProfile
##cProfile.run('keywordize(list_of_articles)')
keywordize(list_of_articles)


#here you make a section to make the list faster and more memory efficient
#eg turn it in a dictionary where keys are frozen sets, and values are the accepted keywords
# faster=
#for article in list_of_articles:
#        faster(article[0],tuple(article[1]),tuple(article[2]))=[[][]]
#        article=()
#
#accordingly, the rest of the code becomes:
#
#for article in list_of_articles:
##    for b in article[1]:
##        for n in range(0,len(list_of_articles)):
##            if list_of_articles[n] == a:
##                continue
##            for k in list_of_articles[n][1]:
##                if Levenshtein.ratio(b,k) >=0.91:
###                    print str(Levenshtein.ratio(b,k))+' '+b+' '+k
##                    a[3].append(b)
##                    count_of_3s_accepted+=1
##                    break
##            else:
##                continue
##            break
##        else:
##            continue
##        break
#


orapiu=datetime.datetime.now()
print 'finished finding candidates. Finding friends... '+str(orapiu-ora)

#either this method, faster with sets but without levenshtein. 
def find_3keys_with_sets(list_of_articles):
    global count_of_3s_accepted
    D=[]
    for a in list_of_articles:
        for b in a[1]:
            D.append(b)
    seen=set()
    seen_add=seen.add
    seen_twice=set(x for x in D if x in seen or seen_add(x))
    count_of_3s_accepted=0
    for a in list_of_articles:
        for g in a[1]:
            if g in seen_twice:
                a[3].append(g)
                count_of_3s_accepted+=1


#or this method, slower with levenshtein (NOT BOTH!)
def find_3keys_with_Levenshtein(list_of_articles):
    global count_of_3s_accepted
    for a in list_of_articles:
        for b in a[1]:
            for n in range(0,len(list_of_articles)):
                if list_of_articles[n] == a:
                    continue
                for k in list_of_articles[n][1]:
                    if Levenshtein.ratio(b,k) >=0.91:
    #                    print str(Levenshtein.ratio(b,k))+' '+b+' '+k
                        a[3].append(b)
                        count_of_3s_accepted+=1
                        break
                else:
                    continue
                break
            else:
                continue
            break


#either this method, faster with sets but without levenshtein. 
def find_2keys_with_sets(list_of_articles):
    global count_of_2s_accepted
    D=[]
    for a in list_of_articles:
        for b in a[2]:
            D.append(b)
    seen=set()
    seen_add=seen.add
    seen_twice=set(x for x in D if x in seen or seen_add(x))
    for a in list_of_articles:
        for g in a[2]:
            if g in seen_twice:
                a[4].append(g)
                count_of_2s_accepted+=1

#or this method, slower with levenshtein (NOT BOTH!)
def find_2keys_with_Levenshtein(list_of_articles):
    global count_of_2s_accepted
    for a in list_of_articles:
        for b in a[2]:
            for n in range(0,len(list_of_articles)):
                if list_of_articles[n] == a:
                    continue
                for k in list_of_articles[n][2]:
                    if Levenshtein.ratio(b,k) >=0.91:
    #                    print str(Levenshtein.ratio(b,k))+' '+b+' '+k
                        a[4].append(b)
                        count_of_2s_accepted+=1
                        break
                else:
                    continue
                break
            else:
                continue
            break

def scrivi(list,file):
    if not not list[3]:
        for u in range(len(list[3])):
                uu=list[3][u]
                file.write("    g.addLink('")
                file.write(uu.replace("'","").replace("\\","").encode('utf8'))
                file.write("', '")
                file.write(list[0].replace("'","").replace("\\","").encode('utf8'))
                file.write("');\n")
    if not not list_of_articles[n][4]:
        for o in range(len(list[4])):
                file.write("    g.addLink('")
                file.write(list[4][o].replace("'","").replace("\\","").encode('utf8'))
                file.write("', '")
                file.write(list[0].replace("'","").replace("\\","").encode('utf8'))
                file.write("');\n")


#find_3keys_with_Levenshstein(list_of_articles)
count_of_3s_accepted=0
find_3keys_with_sets(list_of_articles)
orapiu=datetime.datetime.now()
print 'finished approving and rejecting sequences of 3. Total '+str(count_of_3s_accepted)+' accepted, '+str(orapiu-ora)

#find_2keys_with_Levenshstein(list_of_articles)
count_of_2s_accepted=0
find_2keys_with_sets(list_of_articles)
orapiu=datetime.datetime.now()
print 'finished approving and rejecting sequences of 2. Total '+str(count_of_2s_accepted)+' accepted, '+str(orapiu-ora)
 
n=0
for a in range(0,len(list_of_articles)):
	if not list_of_articles[a][3]:
		n+=1
o=0
for a in range(0,len(list_of_articles)):
	if not list_of_articles[a][4]:
		o+=1

print 'total: '+str(len(list_of_articles))+'. '+str(n)+' Have no accepted sequence of 3. '+str(o)+' Have no accepted sequence of 2. '


for n in range(0,len(list_of_articles), bunch):
    f=open(path+str(n)+'.js','w')
    if n==0:
        f.write("var createGraph = require('ngraph.graph');\n")
        f.write("var g = createGraph();\n")
    else:
        f.write("var g = require('%s.js');\n" %str(n-bunch))
    gg=0
    for v in range(n,n+bunch):
        try:
            scrivi(list_of_articles[v],f)
        except IndexError:
            gg+=1
            if gg==1:
                #f.write("var createLayout = require('ngraph.offline.layout');\n")
                #f.write("var layout = createLayout(g);\n")
                f.write("var save = require('ngraph.tobinary');\n")
                #f.write("layout.run();\n")
                f.write("save(graph);\n")
    f.write('module.export(g)\n')
    f.close()


                
##with open(path+'bello.js','w') as f:
##	f.write("var createGraph = require('ngraph.graph');\n")
##	f.write("var g = createGraph();\n")
##	for n in range(len(list_of_articles)):
##		if not not list_of_articles[n][3]:
##			for u in range(len(list_of_articles[n][3])):
##				uu=list_of_articles[n][3][u]
##				f.write("    g.addLink('")
##				f.write(list_of_articles[n][0].replace("'","").replace("\\","").encode('utf8'))
##				f.write("', '")
##				f.write(uu.replace("'","").replace("\\","").encode('utf8'))
##				f.write("');\n")
##		if not not list_of_articles[n][4]:
##			for o in range(len(list_of_articles[n][4])):
##				f.write("    g.addLink('")
##				f.write(list_of_articles[n][0].replace("'","").replace("\\","").encode('utf8'))
##				f.write("', '")
##				f.write(list_of_articles[n][4][o].replace("'","").replace("\\","").encode('utf8'))
##				f.write("');\n")
##	f.write("var createLayout = require('ngraph.offline.layout');\n")
##	f.write("var layout = createLayout(g);\n")
##	f.write("var save = require('ngraph.tobinary');\n")
##	f.write("layout.run();\n")
##	f.write("save(graph);\n")

orapiu=datetime.datetime.now()
print 'saving to file '+str(orapiu-ora)
