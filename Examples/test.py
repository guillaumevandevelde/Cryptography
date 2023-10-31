ri2 = 1759
ri1 = 550
xi2 = 1
yi2 = 0
xi1 = 0
yi1 = 1
i = -1
quotient = 0

# 1.2
def ext_euclidean(ri1,ri2,i,xi1,yi1,xi2,yi2):

    if ri2 % ri1 == 0 :
        return print(f'Final Iteration {i} : {ri1}')
    
    else:

        if( i == -1 ):
            print(f'i : {i} ')
            print(f'ri : {ri2}')
            print(f'qi :  ')
            print(f'xi : {xi2} ')
            print(f'yi : {yi2}\n')


        if(i == 0 ):
            print(f'i : {i} ')
            print(f'ri : {ri1}')
            print(f'qi :   ')
            print(f'xi : {xi1} ')
            print(f'yi : {yi1}\n')


        if(i > 0):

            ri = ri2 % ri1
            quotient = ( ri2 - ri) / ri1

            xi = xi2 - ( quotient * xi1 )
            yi = yi2 - ( quotient * yi1 )

            print(f'i : {i} ')
            print(f'ri : {ri}')
            print(f'qi : {quotient} ')
            print(f'xi : {xi} ')
            print(f'yi : {yi}\n')
            
            xi2 = xi1
            yi2 = yi1
            xi1 = xi
            yi1 = yi
            ri2 = ri1
            ri1 = ri

        i += 1

        ext_euclidean(ri1,ri2,i,xi1,yi1,xi2,yi2)
    
ext_euclidean(ri1,ri2,i,xi1,yi1,xi2,yi2)