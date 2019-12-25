from re import search
class nomer:
    """
    'NOMER' klasi 
    """
    __nomer=''
    __pattern='^[0][5|7][7|5|1|0][0-9]{7}$'
    format=''
    operator=''
    
    def __init__(self,number):
       
        self.__nomer=number
        
    def nomer(self):
        
        preg=search(self.__pattern,self.__nomer)
        if preg:
            self.format=preg.group()[:3]
            if str(preg.group()[:3]) == str('051' or '050'):
                self.operator='Azercell'
            elif str(preg.group()[:3]) == str('055'):
                self.operator='Bakcell'
            else:
                self.operator='Narmobile'
            return True
        else:
            self.operator='null'
            self.format='null'
            return False







        
