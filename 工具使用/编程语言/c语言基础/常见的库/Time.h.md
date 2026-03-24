# 读取时间
```c
#include <stdio.h>
#include <time.h>

int main(void) {

	time_t tm = time(NULL);

	struct tm* t = localtime(&tm);
	char local_time[100];
	strftime(local_time, sizeof(local_time), "%Y-%m-%d %H:%M:%S", t);
	puts(local_time);

	return 0;
}
}
```