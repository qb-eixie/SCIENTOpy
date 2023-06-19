import pandas as p
import numpy as n
def prodauth(pa):
     f = p.read_csv(pa)
     t = f['Authors']
     ld = [] # duplicate list of all keywords 
     for i in range(len(t)):     
        temp = str(t.loc[i]).split('; ')
        for j in temp: 
            ki = str(t.loc[i]).split('.,')
            for j in ki:
                ld.append((j.lower()))        
     lu = sorted(list(set(ld)))
     fin = []
     for i in range(len(lu)):
        fin.append([])
        fin[i].append(lu[i])
        fin[i].append(ld.count(lu[i]))
     df = p.DataFrame(fin,columns = ['Author', 'Number of publications'] )
     df.sort_values(by = 'Number of publications' ,inplace = True , ascending = False)
     df = df.head(11) 
     c = list(df.columns)
     df.reset_index(drop = True, inplace = True)     
     return (df)
#------------------------------------------------------------------------------------------------------------------------------
def prodyear(pa):
    f = p.read_csv(pa)
    yearsd = []
    for i in f.index:
        yearsd.append(f.iloc[i,3])
    years = list(n.unique(yearsd))
    tdata = []
    for i in range(len(years)):
        tdata.append([])
        tdata[i].append(str(years[i]))
        tdata[i].append(yearsd.count(years[i]))
    df = p.DataFrame(tdata,columns = ['Year of Publication','Number of Publication'] )                
    c = list(df.columns)
    return (df)
#------------------------------------------------------------------------------------------------------------------------------
def authkeys(pa):
     f = p.read_csv(pa)
     t = f['Author Keywords']
     ld = [] # duplicate list of all keywords 
     for i in range(len(t)):     
        temp = str(t.loc[i]).split('; ')
        for j in temp:
            ld.append((j.lower()))        
     lu = sorted(list(set(ld)))
     lu.remove('nan') 
     fin = []
     for i in range(len(lu)):
        fin.append([])
        fin[i].append(lu[i])
        fin[i].append(ld.count(lu[i]))
     df = p.DataFrame(fin,columns = ['Keywords', 'Occurence'] )
     df.sort_values(by = 'Occurence' ,inplace = True, ascending = False )
     df = df.head(11) 
     c = list(df.columns)
     df.reset_index(drop = True, inplace = True)     
     return (df)
#----------------------------------------------------------------------------------------------------

def indkeys(pa):
     f = p.read_csv(pa)
     t = f['Index Keywords']
     ld = [] 
     for i in range(len(t)):     
        temp = str(t.loc[i]).split('; ')
        for j in temp:
            ld.append((j.lower()))        
     lu = sorted(list(set(ld)))
     lu.remove('nan') 
     fin = []
     for i in range(len(lu)):
        fin.append([])
        fin[i].append(lu[i])
        fin[i].append(ld.count(lu[i]))
     df = p.DataFrame(fin,columns = ['Keywords', 'Occurence'] )
     df.sort_values(by = 'Occurence' ,inplace = True, ascending = False)
     l = []
     c = list(df.columns)
     df = df.head(11) 
     c = list(df.columns)
     df.reset_index(drop = True, inplace = True)
     return (df)
#----------------------------------------------------------------------------------------------------

def authpatt(pa):
    f = p.read_csv(pa)
    f = f['Author(s) ID']
    authidlend = []
    for i in f.index: 
        t = str((f.iloc[i])).split(';')
        authidlend.append(len(t))
    authidlenu = list(set(authidlend))
    data = []
    for i in range(len(authidlenu)):
        data.append([])
        data[i].append(str(authidlenu[i]))
        data[i].append(authidlend.count(authidlenu[i]))
    df = p.DataFrame(data , columns = ['Number of Author affliation', 'Occurence'])             
    return (df)
#----------------------------------------------------------------------------------------------------
def prodpubl(pa):
    f = p.read_csv(pa)
    f = f['Publisher']
    f = f.dropna()
    l = list(f.drop_duplicates())
    ld = list(f)
    fin = []
    for i in range(len(l)):
        fin.append([])
        fin[i].append(l[i])
        fin[i].append(ld.count(l[i]))
    df = p.DataFrame(fin, columns = ['Publisher','Number of publications'] )
    df.sort_values(by = 'Number of publications', inplace = True, ascending = False)
    df = df.head(11)
    df.reset_index(drop = True, inplace = True)
    return (df)
#------------------------------------------------------------------------------------------------------    