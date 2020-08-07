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

MicrosoftWebDriver(Edge):https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

#### 目录结构介绍

config:

--config.ini：数据库、邮箱、接口等的配置项，用于方便的调用读取。

data:

--data.xlsx：存放测试数据

framework：

--base_page.py：封装基类，二次封装了定位元素的方法和常见的动作方法

--browser_driver.py：封装了打开浏览器的方法，返回一个浏览器对象

--HTMLTestRunner.py：主要是生成测试报告相关

--logger.py：调用该类的方法，用来打印生成日志

--read_config.py：调用该类的方法，用于读取配置文件

--read_excel：调用该类的方法，用于读取测试用例数据

--send_email.py：这个文件主要是配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑。

logs：

--log：生成的日志文件

pageobjects:

--页面对象：存放各页面中的元素及操作

screenshots:

--png：存放页面截图

test_report:

--report.html：生成的测试报告

testsuites:

--test*.py：存放测试用例

tools:

--driver.exe：存放浏览器驱动

getpathInfo.py：获取项目绝对路径

run.py：开始执行自动化，项目工程部署完毕后直接运行该文件即可

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


