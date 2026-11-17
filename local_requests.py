from requests.models import Response

r = Response()
r.status_code = 200
r._content = '{"姓名":"张三"}'.encode("gbk")
r.headers["Context-Type"] = "text/html"
