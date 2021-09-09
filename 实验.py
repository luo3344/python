import requests
import parsel


# 模拟浏览器发送请求
a = 0
for page in range(0, 5):
    url = 'https://www.ivsky.com/tupian/meinv_t50/index_{}.html'.format(page)
    print(url)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)
    # 把 response.text 文本数据转换成 selector 对象
    print(response)
    selector = parsel.Selector(response.text)
    # 获取所有li标签
    print(selector)
    lis = selector.css('.pli li')
    print(lis)

    # 遍历出每个li标签内容
    for li in lis:
        a = a + 1
        # 获取电影标题 hd 类属性 下面的 a 标签下面的 第一个span标签里面的文本数据 get()输出形式是 字符串获取一个  getall() 输出形式是列表获取所有
        title = li.css('.il_img a img::attr(src)').get()  # get()输出形式是 字符串
        print(title)
        title_url = "https://img-pre.ivsky.com" + title[15:27] + "pre" + title[28:]
        print(title_url)
        response = requests.get(title_url)
        # 在文件保存目录或是Python安装目录下可以找到下载文件
        title1 = str(a) + str('.jpg')
        print("图片：", title1)
        with open(title1, 'wb')as f:
            f.write(response.content)

