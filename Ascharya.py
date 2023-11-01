print("Hi.....")
str1 = '''
python-download-sharepoint-file/sharepoint.py at main

GitHub
https://github.com › iamlu-coding › blob › sharepoint
Contribute to iamlu-coding/python-download-sharepoint-file development by creating an account on GitHub.

List & Download Files from SharePoint Using Python

Python in Plain English
https://python.plainenglish.io › list-download-files-fro...
https://github.com/vgrem/Office365-REST-Python-Client. Create a SharePoint ... The above code will download your files from SharePoi '''
new= str1.replace(' ','')
new =str1.replace('\n','')
# l=list(new)
d={ i:new.count(i) for i in new}
from collections import Counter
# d=Counter(new)
# for i in new:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
print(d)






# max=sal.OvertimePay.max()
# sal[max]
# # print("After removing spaces: ")
# l=list(str1)
# print(l)

# print("count with spaces:",)
