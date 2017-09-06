#include <iostream>
using namespace std;
#define ll long long
int main()
{
	ll n,k,a[10001],i,lo,hi,mid,ans,tmp,c;
	cin>>n>>k;
	for(i=0;i<n;i++)
		cin>>a[i];
	lo = 1;
	hi = 1000000000;
	while(lo<=hi)
	{
		mid = (lo + hi)/2;
		c = 0;
		for(i=0;i<n;i++)
		{
			if(a[i]%mid!=0)
			{
				tmp = a[i]/mid;
				c += (((tmp+1)*mid)-a[i]);
			}
		}
		if(c<=k)
		{
			ans = mid;
			lo = mid + 1;
		}
		else
			hi = mid - 1;
		cout<<ans<<endl;
	}
	cout<<ans<<endl;
	return 0;
}