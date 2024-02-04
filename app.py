from itertools import islice
from duckduckgo_search import DDGS
from flask import Flask, request

app = Flask(__name__)


def run():
    if request.method == 'POST':
        data = request.get_json()  # 获取 JSON 数据
        keywords = data['q']
        max_results = int(data.get('max_results', 10))
    else:
        keywords = request.args.get('q')
        # 从请求参数中获取最大结果数，如果未指定，则默认为10
        max_results = int(request.args.get('max_results', 10))
    return keywords, max_results


@app.route('/search', methods=['GET', 'POST'])
async def search():
    keywords, max_results = run()
    results = []
    with DDGS() as ddgs:
        # 使用DuckDuckGo搜索关键词
        ddgs_gen = ddgs.text(keywords,safesearch='Off', timelimit='y', backend="lite")
        # 从搜索结果中获取最大结果数
        for r in islice(ddgs_gen, max_results):
            results.append(r)

    # 返回一个json响应，包含搜索结果
    return {'results': results}

@app.route('/searchNews', methods=['GET', 'POST'])
async def search_news():
    keywords, max_results = run()
    results = []
    with DDGS() as ddgs:
        # 使用DuckDuckGo搜索关键词
        ddgs_news_gen = ddgs.news(keywords, safesearch="off", timelimit="m")
        # 从搜索结果中获取最大结果数
        for r in islice(ddgs_news_gen, max_results):
            results.append(r)
    # 返回一个json响应，包含搜索结果
    return {'results': results}

@app.route('/searchAnswers', methods=['GET', 'POST'])
async def search_answers():
    keywords, max_results = run()
    results = []
    with DDGS() as ddgs:
        # 使用DuckDuckGo搜索关键词
        ddgs_gen = ddgs.answers(keywords)
        # 从搜索结果中获取最大结果数
        for r in islice(ddgs_gen, max_results):
            results.append(r)

    # 返回一个json响应，包含搜索结果
    return {'results': results}


@app.route('/searchImages', methods=['GET', 'POST'])
async def search_images():
    keywords, max_results = run()
    results = []
    with DDGS() as ddgs:
        # 使用DuckDuckGo搜索关键词
        ddgs_gen = ddgs.images(keywords, safesearch='Off', timelimit=None)
        # 从搜索结果中获取最大结果数
        for r in islice(ddgs_gen, max_results):
            results.append(r)

    # 返回一个json响应，包含搜索结果
    return {'results': results}


@app.route('/searchVideos', methods=['GET', 'POST'])
async def search_videos():
    keywords, max_results = run()
    results = []
    with DDGS() as ddgs:
        # 使用DuckDuckGo搜索关键词
        ddgs_gen = ddgs.videos(keywords, safesearch='Off', timelimit=None, resolution="high")
        # 从搜索结果中获取最大结果数
        for r in islice(ddgs_gen, max_results):
            results.append(r)

    # 返回一个json响应，包含搜索结果
    return {'results': results}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
