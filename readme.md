## <center> **我的自动化测试框架**</center>

---
#### 关于框架：
框架基于python3 + selenium + unittest + HTMLTestRunner搭建的WebUI自动化测试框架

#### 特点：
- 使用POM（页面对象模式）设计，使代码更加有逻辑性，测试脚本更加规范，后期更加容易维护以及复用性更高
- 支持多种定位方式，包括（xpath/css/ID/text/link_text/name）
- 框架集成了Selenium的常用定位方法，使元素定位更加方便
- 使用HTMLTestRunner作为自动生成测试报告，报告更加美观，更加详细，内容更丰富
- Logging日志输出，可以看到每一步做的操作

#### 部署环境：
- Python 3.6+：https://www.python.org/

#### 使用到的package：

> pip install requirements.txt

#### 支持的浏览器及驱动：
基于Selenium支持的所有浏览器

```
browser == "Chrome"
browser == "firefox"
browser == "IE"
```
geckodriver(Firefox):https://github.com/mozilla/geckodriver/releases

Chromedriver(Chrome):https://sites.google.com/a/chromium.org/chromedriver/home

IEDriverServer(IE):http://selenium-release.storage.googleapis.com/index.html

operadriver(Opera):https://github.com/operasoftware/operachromiumdriver/releases

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

#### 定位元素方式：

```
class BaiduPage(BasePage):
    """
    在这里写定位器，通过元素属性定位元素对象
    """
    search_loc =(By.XPATH,'//*[@id="kw"]')#定位百度文本框

    def input_baidu_text(self,text):
        self.send_key(self.search_loc,text)
```


#### 日志输出

```
2020-08-07 11:42:51,560 - INFO - 打开的用例数据文件为F:\Python\uiautomation_framework/data/data.xlsx
2020-08-07 11:42:51,566 - INFO - 选择的浏览器为 Firefox
2020-08-07 11:42:51,566 - INFO - 打开的URL为：https://www.baidu.com/
2020-08-07 11:43:00,644 - INFO - 启动火狐浏览器
2020-08-07 11:43:03,584 - INFO - 设置5秒隐式等待时间
2020-08-07 11:43:03,585 - INFO - 清空文本框内容kw
2020-08-07 11:43:04,745 - INFO - 输入内容python
2020-08-07 11:43:11,526 - INFO - 页面已截图，截图的路径在:F:\Python\uiautomation_framework/screenshots/
2020-08-07 11:43:12,121 - INFO - 选择的浏览器为 Firefox
2020-08-07 11:43:12,121 - INFO - 打开的URL为：https://www.baidu.com/
2020-08-07 11:43:20,214 - INFO - 启动火狐浏览器
2020-08-07 11:43:22,295 - INFO - 设置5秒隐式等待时间
2020-08-07 11:43:22,295 - INFO - 清空文本框内容kw
2020-08-07 11:43:23,415 - INFO - 输入内容selenium
2020-08-07 11:43:30,365 - INFO - 页面已截图，截图的路径在:F:\Python\uiautomation_framework/screenshots/
2020-08-07 11:43:32,044 - INFO - 邮件发送成功！！！
```

#### 生成测试报告，发送邮件

```
	def run(self):
		now = time.strftime("%Y-%m-%d_%H_%M_%S_")
		report_name = pro_dir + '/test_report/' + now + 'result.html'
		try:
			suit = self.set_case_suite()
			if suit is not None:

				fp = open(report_name, 'wb')
				runner = HTMLTestRunner.HTMLTestRunner(
					stream=fp,
					title="测试报告",
					description="测试用例执行情况"
				)
				runner.run(suit)
				fp.close()
			else:
				print("Have no case to test.")
		except Exception as e:
			print(str(e))
		finally:
			print("*"*5 + "TEST END" + "*"*5)
		if on_off == "on":
			SendEmail().send_email(report_name)
		else:
			print("邮件发送开关配置关闭，请打开开关后可正常自动发送测试报告")
```


