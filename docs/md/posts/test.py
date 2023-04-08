import pandas as pd
import os

import pathlib

# path = "/Users/hg/WORKSPACE/Gitblog/mkdocs-material/docs/md/posts/덕산테코피아_소재_투자"


def markdownImageLink(fname):
    
    file = pathlib.Path(f"/Users/hg/WORKSPACE/Gitblog/mkdocs-material/docs/md/posts/{fname}")
    df = pd.DataFrame()
    if file.exists ():
        
   
        filenamelist=os.listdir(f"/Users/hg/WORKSPACE/Gitblog/mkdocs-material/docs/md/posts/{fname}")
        # filenamelist = filenamelist.pop(-1)
        # filenamelist=makeHtml(fname,filenamelist)
        df["이미지"] = filenamelist
        dfs = df[~df['이미지'].str.contains("json", na=False, case=False)]
        dfs = dfs.sort_values(by=['이미지'], axis=0, ascending=True)
        dfs["이미지"]=f"!LRBraket(/images/"+f"{fname}/"+dfs["이미지"]+")"
        mkImageLists = dfs["이미지"].tolist()
        # print(mkImageLists)
        return [mkImageLists,mkImageLists,mkImageLists]
    else:
        
        return "none"
  


print (markdownImageLink("덕산테코피아_소재_투자"))