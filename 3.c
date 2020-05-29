#include<stdio.h>
int main()
{
  int a=0,b=0,c=0;
  for(int i=0;i<8;i++)
    {
      a+=2;
      for(int j=0;j<8;j++)
	{
	  b+=a;
	  c-=b;
	}
    }
  if(a>b&&b<c)
    {printf("yeah I will go ahead and a=%d b=%d c=%d\n",a,b,c);}
  else
    {
      printf("otherwise i will cose my system a=%d.b=%d.c=%d.\n",a,b,c);
    }
}
