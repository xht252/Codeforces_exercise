#include<iostream>

using namespace std;

int n , m;

int main()
{
	cin >> n >> m;
	for(int i = 0;i < n;i ++)
	{
		string s;
		cin >> s;
		for(int j = 0;j < m;j ++)
		{
			if(s[j] == '-') continue;
			
			if((i + j) % 2) s[j] = 'W';
			else s[j] = 'B';
		}
		cout << s << endl;
	}
	return 0;
}
