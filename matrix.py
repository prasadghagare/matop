import re
class Matrix:
    def __init__(self,name,rows=1,columns=1,mat_string='[1;1]'):
        self.name = name
        self.no_of_rows = rows
        self.no_of_columns = columns
        self.mat_dict = {}
        self.mat_string = mat_string
        k = self.mat_string.find('[')
        print 'k',k
        l = self.mat_string.find(']')
        print 'l',l
        le = len(self.mat_string)
        print 'le',le
        nums = re.findall(r'[\d]+', self.mat_string)
        #print bool_total_elem
        if k !=0 or l != le - 1 or (self.no_of_columns * self.no_of_rows == len(nums)) == False:
            print 'missing square brackets'
        else:
            i = 0
            while (i < len(nums)):
                for j in range(1,self.no_of_rows + 1):
                        for t in range(1,self.no_of_columns + 1):
                                self.mat_dict.update({(j,t):nums[i]})
                                i = i + 1

#    def add():
#  "overload + operator here"


#testing the class made
#making a 4*4 matrix with all elements 1
if __name__ == '__main__':
   # matr_4_4 = Matrix("M",4,4)
    matr_4_4 = Matrix("M", 3 , 2 ,'[11 2;4 3 :5 33]')
    print matr_4_4.mat_dict