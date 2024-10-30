# 🌟 Google Translate 双向多次翻译脚本

## 📖 介绍

这个 Python 脚本使用 Selenium 实现了 Google 翻译的双向翻译功能。您可以输入任意文本，设置翻译的轮数，脚本将自动进行中文和英文之间的翻译，并将结果保存到 `translation.txt` 文件中。

## 🛠️ 安装依赖

在使用该脚本之前，确保您已经安装了以下软件：

1. **Python 3.x**：确保已安装 Python。
2. **Selenium**：如未安装会自动运行安装命令。

您也可以手动安装 Selenium：

```bash
pip install selenium
```

## 📦 下载 ChromeDriver

该脚本依赖于 ChromeDriver。请确保下载与您的 Chrome 浏览器版本相对应的 ChromeDriver，并将其添加到系统 PATH 中。您可以在 ChromeDriver 官方网站 下载。

## 🚀 使用方法

1. **编辑文本**： 修改脚本中的 `text` 变量，输入您想要翻译的文本。

   ```python
   text = """
   这里是需要翻译的文本。
   """
   ```

2. **设置翻译轮数**： 通过修改 `times` 变量设置翻译的轮数（默认是 5 轮）。

   ```python
   times = 5
   ```

3. **运行脚本**： 在终端中执行脚本：

   ```bash
   python translate.py
   ```

4. **查看结果**： 翻译结果将打印在终端中，同时保存在 `translation.txt` 文件中。您可以在同一目录下找到该文件。

## ⚙️ 脚本结构

- **函数 `translate`**：执行翻译操作，获取翻译结果。
- **主循环**：在指定次数内进行双向翻译，并记录每一轮的结果。
- **异常处理**：捕获和打印任何运行时错误。

## 📝 注意事项

- **网络连接**：确保在运行脚本时有稳定的互联网连接。
- **翻译速度**：由于可能受到 Google 的限制，翻译操作可能需要一些时间（翻译一轮需要**10秒以上**），请耐心等待。
- **文本格式**：确保输入文本的格式正确，以避免翻译结果出现问题。