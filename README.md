# excel2json v1.0.0

#### 概述

excel 文件转 json python3.x

#### 配置

| 属性   | 说明            | 类型   | 必填 | 默认值 |
| ------ | --------------- | ------ | ---- | ------ |
| fields | 表头字段        | Array  | 是   | -      |
| input  | excel 入口文件  | String | 是   | -      |
| output | json 输出文件名 | String | 是   | -      |

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
