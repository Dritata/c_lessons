#include <stdio.h>
#include <stdint.h>

union int_to_char{
uint64_t uint64_buf;
uint32_t uint32_buf[2];
unsigned char uchar_buf[8];
};

int main(void)
{
unsigned char  uch_buf[8];
union int_to_char itc;

for(unsigned char i = 0; i < 8; i++)
{
  //uch_buf[i]=0xFF;
  itc.uchar_buf[i] = i;
}
//itc.uint64_buf=0xFFFFFFFFFFFFFFFF;

//printf("Hello, world! %ld \n", *itc.int64_buf);
for(int i = 0; i < 8; i=i+1)
{
  printf("Hello, world! %c \n", itc.uchar_buf[i]);
}

return 0;
}
