from operator import index
"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------
Este archivo contiene las preguntas que se van a realizar en el laboratorio.
Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.
"""
import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    return tbl0.shape[0]

def pregunta_02():
    return tbl0.shape[1]

def pregunta_03():
    return(tbl0.groupby("_c1")["_c1"].count())

def pregunta_04():
    return(tbl0.groupby("_c1")["_c2"].mean())

def pregunta_05():
    return(tbl0.groupby("_c1")["_c2"].max())

def pregunta_06():
    return((list(map(lambda x: x.upper(), sorted(tbl1._c4.unique())))))

def pregunta_07():
    return(tbl0.groupby("_c1")["_c2"].sum())

def pregunta_08():
    tbl0["suma"]=tbl0.sum(axis=1, numeric_only=True)
    return(tbl0)

def pregunta_09():
    tbl0['year']=list(map(lambda x: x[0:4], list(tbl0.loc[:,"_c3"])))
    return(tbl0)

def pregunta_10():
    listas = tbl0.groupby(['_c1'])['_c2'].apply(list).tolist()
    _c2=[]
    for lista in listas:
      texto=""
      for num in sorted(lista):
        texto+=f'{num}:'
      _c2+=[texto[:-1]]
    return(pd.DataFrame({'_c2': _c2}, index = pd.Series(['A', 'B', 'C', 'D', 'E'], name='_c1')))

def pregunta_11():
    listas = tbl1.groupby(['_c0'])['_c4'].apply(list).tolist()
    _c0 = tbl1['_c0'].unique().tolist()
    _c4=[]
    for lista in listas:
      texto=""
      for num in sorted(lista):
        texto+=f'{num},'
      _c4+=[texto[:-1]]
    return(pd.DataFrame({'_c0':_c0, '_c4': _c4}))

def pregunta_12():
    listas1 = (tbl2.groupby(['_c0'])['_c5a'].apply(list).tolist())
    listas2 = (tbl2.groupby(['_c0'])['_c5b'].apply(list).tolist())
    _c0 = tbl2['_c0'].unique().tolist()
    _c5=[]
    for index in range(0,len(listas1)):
      texto=""
      for index1 in range(0,len(listas1[index])):
        texto+=f'{listas1[index][index1]}:{listas2[index][index1]}, '
      _c5+=[",".join(sorted(texto.split(', '))[1:])]
    return(pd.DataFrame({'_c0':_c0, '_c5': _c5}))

def pregunta_13():
    tbl0_2 = pd.merge(tbl0, tbl2, on='_c0', how='inner')
    return(tbl0_2.groupby("_c1")["_c5b"].sum())
