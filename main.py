

inf = 9999
def main():
    n = int(input())
    empArr = list(map(int,input().split()))
    empArr.insert(0,inf)
    empArr.append(inf)
    hikeArr = [0]*(n+2)
    for i in range(1,n+1):
        if(empArr[i-1] >= empArr[i] and empArr[i<=empArr[i+1]]):
            hikeArr[i] = 1
    for i in range(1,n+1):
        if(empArr[i-1]<empArr[i] and empArr[i]<= empArr[i+1]):
            hikeArr[i] = hikeArr[i-1]+1
    for i in range(1,n+1):
        if(empArr[i-1]>=empArr[i] and empArr[i]>empArr[i+1]):
            hikeArr[i] = hikeArr[i+1]+1
    for i in range(1,n+1):
        if(empArr[i-1]<empArr[i] and empArr[i]>empArr[i+1]):
            hikeArr[i] = max(hikeArr[i-1],hikeArr[i+1])+1
    for i in range(1,n+1):
        print(hikeArr[i], end = " ")
if __name__ == '__main__':
   main()