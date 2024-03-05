#include <iostream>
using namespace std;
int count_As(int a[],int n)
{
     int count=0,i;
    for(i=0;i<n;i++)
    {
        if(a[i]=='a')
        {
            count++;
        }
    }
    return count;
}\/
int main()
{
    int n,i,c;
    cout<<"enter the array size";
    cin>>n;
    int a[n];
    cout<<"enter the character in array";
    for(i=0;i<n;i++)
    {
        cin>>a[i];
    }
    c=count_As(a,n);
    cout<<n;
    return 0;
    
    
}