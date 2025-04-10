# Flask 示例应用 - 任务管理器

这是一个使用 Flask 框架构建的简单任务管理应用，演示了 Flask 的基本功能。

## 功能

- 查看任务列表
- 添加新任务
- 将任务标记为完成/未完成
- 删除任务
- 使用 Flash 消息提供用户反馈

## 技术特点

- 路由和视图函数
- 表单处理
- 模板渲染使用 Jinja2
- 重定向和 URL 生成
- 闪现消息 (Flash messages)

## 运行应用

1. 确保已安装 Flask：
   ```
   pip install flask
   ```

2. 运行应用：
   ```
   python app.py
   ```

3. 在浏览器中访问 http://127.0.0.1:5000/ 查看应用

## 项目结构

```
/sample_app
  ├── app.py            # 主应用文件
  ├── templates/        # HTML 模板
  │   └── index.html    # 主页模板
  └── README.md         # 项目说明
```

## 学习目标

这个简单的应用演示了以下 Flask 核心概念：

- 创建和配置 Flask 应用实例
- 定义路由和视图函数
- 使用请求对象获取表单数据
- 使用 Jinja2 模板引擎渲染 HTML
- 使用 Flash 提供用户反馈
- 使用 URL 重定向和 URL 构建

这个示例应用可以作为学习 Flask 框架的起点，也可以作为构建更复杂 Web 应用的基础。
