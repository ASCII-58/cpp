#include <iostream>
#include <string>
#include <windows.h>
#include <cmath> // ����cmath����ʹ��sqrt����
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
					
					cout << output << j << endl;
					// ���Ӽ�����
					for (int k = 0; k < 4000000; k++)
					{
						double x = sqrt(k);
					}
				}
			}
			output += string1[i];
		}
		else
		{
			output += ' ';
			cout << output << endl;
		}
	}
	cout << string1 << endl;
}
