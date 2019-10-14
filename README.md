# itree v1.0.5

#### 概述

excel 文件转 json python3.x

#### 配置

```json
{
	// 表头字段
	"fields": ["name", "age", "sex"],
	// excel入口文件
	"input": "1班童鞋.xlsx",
	// json输出文件名
	"output": "students"
}
```

#### 输出

```json
[
	{
		"name": "1号童鞋",
		"age": 10.0,
		"sex": "男"
	},
	{
		"name": "2号童鞋",
		"age": 12.0,
		"sex": "女"
	},
	{
		"name": "3号童鞋",
		"age": 10.0,
		"sex": "男"
	}
]
```

#### 作者

SuperIron
