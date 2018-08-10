class poly:
    #constructor
    def __init__(self, coefs):
        #initializing the variables -- cast to float 
        self.coefs = [float(coefs) for coefs in coefs]
        self.degree=len(coefs)-1
        self.rep = self.__str__()
        
    def __str__(self):
        #for string conversion of the polynomial
        if len(self.coefs)==0:
            return str(0)
        
        polynomial=''

        if self.coefs[0]!=0:
            if self.coefs[0]<0:
                polynomial += str(self.coefs[0])
            else:
                polynomial += '+' + str(self.coefs[0])
        if self.coefs[1]!=0:
            if self.coefs[1]<0:
                polynomial += str(self.coefs[1])+'X'
            else:
                polynomial += '+' + str(self.coefs[1])+ 'X'

        index = 2  
        while index < len(self.coefs):
            if self.coefs[index] != 0:
                if self.coefs[index] < 0:
                    polynomial += str(self.coefs[index]) + 'X^' + str(index)
                else:  
                    polynomial += '+' + str(self.coefs[index]) + 'X^' + str(index)
            index+=1

        return polynomial
   
   #for printing 
    def __repr__(self):
        return self.rep
       
    #takes the coeffcient parameters
    def __getitem__(self, k):
        if k < len(self.coefs):
            return self.coefs[k]
        
    #does addition with another poly
    def __add__(self, other):
        polysum=[]
        for i in range(len(self.coefs)):
            polysum.append(self.coefs[i] + other.coefs[i])
        return poly(polysum)
    
    #multiplication with poly for float
    def __mul__(self,other):
        num = self.degree + other.degree
        product = [0]*(num+1)
        for i in range(0, self.degree + 1):
            for j in range(0, other.degree + 1):
                product[i+j] += self.coefs[i] * other.coefs[j]
        return poly(product)
        
    #multiplication for poly ---int
    def __rmul__(self,other):
        if type(self) != type(other):
            if type(other) == int or type(other) == float:
                for x in self.coefs:
                    return other*x 
            else:
                raise NotImplementedError
            
    #test two polys for equality
    def __eq__(self,other):
        if len(self.coefs)!=len(other.coefs):
            print('False')
            return False
        elif len(self.coefs)==len(other.coefs):
            for i in range(len(self.coefs)):
                if self.coefs[i] != other.coefs[i]:
                    print('False')
                    return False
            print('True')    
            return True

    #test two polys for equality
    def __ne__(self,other):
        if len(self.coefs)!=len(other.coefs):
            print('True')
            return True
        elif len(self.coefs)==len(other.coefs):
            for i in range(len(self.coefs)):
                if self.coefs[i] != other.coefs[i]:
                    print('True')
                    return True
            print('False')    
            return False

    #evaluation for current poly 
    def eval(self, x):
        eval=0
        if type(x) == list:
            print('in eval')
            eval = [self.__init__(i) for i in x]
            return eval

        elif type(x)==float or type(x)==int:
            for i in range(len(self.coefs)):
                eval += self.coefs[i] * pow(x, i)#
            return eval 


def test_poly():
    p1 = poly([1, -2, 1])    # poly of grade 2: p1(X)=1-2X+X2 
    p2 = poly((0, 1))        # create poly of grade 1 with a tuple: p2(X)=X, (a0==0)
    print(p1)                # print calls __str__ and prints 1.0-2.0X+X^2
    p1                       # python calls __repr__ and displays 1.0-2.0X+X^2
    p1 == p2                 # returns False 
    p1 == poly((1, -2, 1))   # return True 
    p1 != p2                 # returns True
    
    p3 = p1 + p2             # sum, __add__ 
    print(p3)                # prints 1.0-X+X^2.0   (use default number of decimals)
    
    p1[1]                    # indexing the coefficients: returns -2 (a1 for p1)
    
    p4 = p2 * p1             # product with another Poly: p4 becomes X-2X^2+X^3 
    p5 = p1 * 2              # product with int or float: p5 becomes 2-4X+2X^2 
    p6 = 3 * p1              # product with int or float: p6 becomes 3-6X+3X^2 (__rmul__)
    
    print( p1.eval(2) )      # evaluate p1 at point 2: prints 1.0 
    print( p1.eval([0,-1,1]) # evaluate p1 for a list of points: prints [1,4,0]
        

test_poly()     #wtf