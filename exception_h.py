try:  
	f=open("read.txt","r")
	if f.name=="read.txt":        
		raise Exception 

	# var=var_a  
except FileNotFoundError:   
	print("File Not Found")
except Exception as e:  
	print(e)
else:  
	print(f.read())