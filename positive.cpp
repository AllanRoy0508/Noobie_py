#include <iostream>
using namespace std;

int main() {
	 int n;
    cout<<"Enter the number";
    cin>>n;
    if(n==0)
	  {
	  	cout<<"Zero";
	  }
    if(n>0)
      {
        cout<<"Positive";
      }
    if(n<0)
      {
        cout<<"Negative";
      }
	return 0;
}
