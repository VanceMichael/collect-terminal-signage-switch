# 航站楼演出移场后的屏端采集与换播

本服务用于在本机读取业务来源的合成记录。各来源路径从首页进入，其字段和时间含义见[资料提供方的格式](docs/来源契约.md)。

柜台页面可用 Chromium 浏览。复用预装的 Python 3.11 和 Playwright 1.56.0 环境时可直接运行。在新环境可运行 `python3 -m pip install -r requirements.txt`，然后运行 `python3 -m playwright install chromium`。

使用 `python3 source_server.py` 启动，在浏览器打开 `http://127.0.0.1:8040/`。本地样本保存在 `origins/`，按资料方路径分开。柜台受理页使用合成票号，返回的是该柜台的观测。

运行 `python3 -m unittest -v` 检查资料站能实际提供可读取的原件和浏览器回执。
