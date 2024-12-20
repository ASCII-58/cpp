#include <iostream>
#include <string>
#include <windows.h>
using namespace std;

int main()
{	
	string space = " ";
	string output = "";
	string string1 = "Hello World";
	for (int i = 0; i < string1.length(); i++)
	{
		if (string1[i] != ' ')
		{
			for (char j = 65; j < string1[i]; j++)
			{
				if (!(j >= 65 && j <= 90 || j >= 97 && j <= 122))
				{
					continue;
				}
				else
				{
					Sleep(5);
					cout << output << j << endl;
				}
			}
			output += string1[i];
		}
		else
		{
			output += ' ';
			cout << output << endl;
		}
	}cout << string1<< endl;
	return 0;
}
