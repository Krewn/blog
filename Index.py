import os

class indexer:
	path = "~"
	site = "http://krewn.github.io"
	proj = "blog"
	prod = []
	loc=[]
	
	def __init__(self,p):
		self.path=p
	def fprep(self,name):
		name.replace(".","")
		name.replace("\\","/")
		name.replace("?","%3F")
		name.replace(" ","%20")
		return(name)
	def refPrep(self):
		ref = self.site+"/"+self.proj
		for qw in self.loc:
			ref+="/"+qw
		return(ref)
	def HtmlFrek(self,adir):
		self.loc.append(adir)
		os.chdir(adir)
		ret="<h2>"+adir+"</h2>"
		files = [f for f in os.listdir('.') if os.path.isfile(f) and f.split(".")[len(f.split("."))-1]=="html"]
		for t in files:
			ret+="<a href ="+self.refPrep()+"/"+self.fprep(t)+">"+self.fprep(t)+"</a><br>\n"
		images = [f for f in os.listdir('.') if os.path.isfile(f) and f.split(".")[len(f.split("."))-1]=="png"]
		for i in images:
			i = self.fprep(i)
			ref = self.refPrep()
			ret+= "<img src="+ref+"/"+i+"><br>\n"
		folders = [f for f in os.listdir(".") if not os.path.isfile(f)]
		for k in folders:
			if(k.__contains__(".")):
				continue
			ret+="<div class='blue1'>"
			ret+=self.HtmlFrek(k)
			ret+="</div>"
		os.chdir("..")
		del self.loc[len(self.loc)-1]
		return(ret)
		
	def HtmlProd(self):
		print("start")
		ret = ""
		ret+="""<!DOCTYPE html><html>"""
		ret+="<div>"
		files = [f for f in os.listdir('.') if os.path.isfile(f) and f.split(".")[len(f.split("."))-1]=="html"]
		for t in files:
			ret+="<a href ="+self.refPrep()+"/"+self.fprep(t)+">"+self.fprep(t)+"</a><br>\n"
		folders = [f for f in os.listdir(".") if not os.path.isfile(f)]
		for k in folders:
			if(k.__contains__(".")):
				continue
			print k
			ret+="<div>"
			ret+=self.HtmlFrek(k)
			ret+="</div>"
		ret+="</div>"
		ret+="""</html>"""
		self.prod = ret
		return(ret)
		
i = indexer(".")
q=i.HtmlProd()
#print i.prod

w = open("index.html","w")
w.write(q)
w.close()
