# 人工智能
# 开发人：高云龙
# 开发时间：2022/9/21  14:00
class RoutrYearConverter:
    regex = '[0-9]{4}'
    def to_python(self,value):
        return int(value)
    def to_urls(self,value):
        return '%04d' % value