def add(n1, n2):
 if n1=="" or n2=="":
  return "Invalid Operation"
 if n1 is None or n2 is None:
  return "Invalid Operation"
	
 n1=int(n1)
 n2=int(n2)
 answer=n1+n2
 answer=str(answer)
 return answer
