def merge(arr,beg,mid,end):
              n1=mid-beg+1
              n2=end-mid
              i=j=0
              left=arr[beg:mid+1]
              right=arr[mid+1:end+1]
              k=beg
              while i<n1 and j<n2:
                if left[i]<=right[j]:
                   arr[k]=left[i]
                   i+=1
                else: 
                  arr[k]=right[j]
                    j+=1
                k+=1
               while i<n1:
                 arr[k]=left[i]
                 k+=1
                 i+=1         
               while j<n2:
                 arr[k]=right[j]
                 k+=1
                 i+=1                   
         def mergesort(arr,beg,end):
             if beg<end:
                mid =(beg+end)//2
                mergesort(arr,beg,mid)
                mergesort(arr,mid+1,end)
                merge(arr,beg,mid,end)
         a=[8,7,6,4,3,2,1]
         b=0
         e=len(a)-1
         mergesort(a,b,e)
         print(a)
