- vs中， 调用M_PI需要加载`_USE_MATH_DEFINES`
```c
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

int main(void) {

	double num = 1.0;
	sin(num); // 正弦函数
	asin(num); // 反正弦函数
	sinh(num);	// 双曲正弦函数
	exp(num); // 以e为底的指数函数
	log(num); // 以e为底的对数函数
	log2(num); // 以2为底的对数函数
	log10(num); // 以10为底的对数函数
	sqrt(num); // 平方根函数
	fabs(num); // 绝对值函数
	ceil(num); // 向上取整函数
	floor(num); // 向下取整函数
	fmod(num, 0.5); // 取模函数
	pow(num, 2.0); // 幂函数

	printf("The value of M_PI is: %f\n", M_PI); 

	return 0;
}
```
