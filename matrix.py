import re
class Matrix:
    def __init__(self,name,rows=1,columns=1,mat_string='[1;1]'):
        self.name = name
        self.no_of_rows = rows
        self.no_of_columns = columns
        self.mat_dict = {}
        self.mat_string = mat_string
        k = self.mat_string.find('[')
        l = self.mat_string.find(']')
        le = len(self.mat_string)
        self.nums_string = re.findall(r'[\d]+', self.mat_string)
        #num = []
        #for i in range(len(self.nums_string)):
         #   num.append(  int(self.nums_string[i]))

        num = [int(self.nums_string[i]) for i in range(len(self.nums_string))]

        #print bool_total_elem
        if k !=0 or l != le - 1 or (self.no_of_columns * self.no_of_rows == len(self.nums_string)) == False:
            print 'missing square brackets'
        else:
            i = 0
            while (i < len(self.nums_string)):
                for j in range(1,self.no_of_rows + 1):
                        for t in range(1,self.no_of_columns + 1):
                                self.mat_dict.update({(j,t):num[i]})
                                i = i + 1

    def __add__(self,other):
        #return self.mat_dict[(1,1)] + other.mat_dict[(1,1)]
        if self.no_of_columns * self.no_of_rows != other.no_of_columns * other.no_of_rows:
            print 'please ensure dimension of both matrices are same and retry'
        else:
            m = 0
            mat_add = Matrix('mat_add', self.no_of_rows, self.no_of_columns, self.mat_string)
            while (m < len(self.nums_string)):
                for i in range(1,self.no_of_rows + 1):
                    for j in range(1, self.no_of_columns + 1):
                        mat_add.mat_dict.update({(i,j) : self.mat_dict[(i,j)] + other.mat_dict[(i,j)]})
                        m = m + 1

            return mat_add

#testing the class made
#making a 4*4 matrix with all elements 1
if __name__ == '__main__':
   # matr_4_4 = Matrix("M",4,4)
    matr_4_4 = Matrix("M", 3 , 2 ,'[11 2;4 3 :5 33]')
    mat_tmp = Matrix('M2', 1, 1, '[1]')
    print matr_4_4 + mat_tmp

    print matr_4_4.mat_dict