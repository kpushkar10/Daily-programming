#include <iostream>

int main()
{
  int a;
  std::cout<< "Enter number: ";
  std::cin>>a;
  if(a%6 == 0)
    std::cout<< a<< " is divisible by 6"<<std::endl;
  else
    std::cout<<a<< " is not divisible by 6"<<std::endl;
}