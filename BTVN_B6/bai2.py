def matrix_t(matrix):
    y=[]
    j=0
    t=[]
    while j<len(matrix):
        row=[]
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        t.append(row)
        j+=1
    for row in t:
        print(*row)
def main():
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    matrix_t(matrix)
main()

