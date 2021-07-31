import requests
import re
import os

headers = {
    "Accept-Encoding": "Gzip",
    "User-Agent": "Mozilla/5.0 (Window NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
}

# 搜索页面数据
def get_text(keyword, page):
    url = f"https://www.doutula.com/search?type=photo&more=l&keyword={keyword}&page={page}"
    # 请求数据
    resp = requests.get(url, headers=headers)
    # 去掉非字符
    text = re.sub('\s', '', resp.text)
    return text


def down_meme(keyword):
    pages = 5
    num = 0
    for page in range(1, pages+1):
        text = get_text(keyword, page)
        # 表情包区域
        search_result = re.findall(r'divclass="search-resultlist-group-item"(.*?)class="text-center"', text)[0]
        # 表情包下载地址
        meme_urls = re.findall(r'"data-original="(.*?)"', search_result)

        # 下载每页的表情包
        for meme_url in meme_urls:
            num += 1
            # 表情包文件名
            meme_name = re.findall(r'http://img.doutula.com/.*/(.*)', meme_url)[0]
            meme_img = requests.get(meme_url)
            # 表情包内容byte格式
            meme = meme_img.content
            # 写入本地
            if not os.path.exists(f'./{keyword}'):
                os.mkdir(f'./{keyword}')

            with open(f'./{keyword}/{meme_name}', 'wb') as f:
                f.write(meme)

            print(f'{num} 个 {keyword} 表情包已经下载')


if __name__ == "__main__":
    keyword = input("请输入查询的表情包：")
    down_meme(keyword)