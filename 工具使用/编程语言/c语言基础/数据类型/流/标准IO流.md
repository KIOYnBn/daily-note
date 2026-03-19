## 输入
- scanf_s
	- `Note`: 当输入字符串时， 需要标注缓存区大小， 其他变量不需要
```c
#include <stdio.h>

int main(void) {

	char str[50] = { 0 };
	scanf_s("%49s", str, (unsigned int)sizeof(str));
	puts(str);

	int num;
	int result = scanf_s("%d", &num);
	if (result == 1) {
		printf("This number is %d\n", num);
	}
	else if (result == EOF) {
		puts("Reaching end");
	}
	else {
		puts("input a invalid number");
	}

	

	char ch;
	scanf_s(" %c", &ch, 1);
	printf("This char is %c", ch);

	return 0;
}
```
