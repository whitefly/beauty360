from scrapy import Request
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline


class Pipeline_image(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 返回一个放图片url的request
        yield Request(item['url'])

    def file_path(self, request, response=None, info=None):
        # 用来定义图片的名字(含后缀)
        url = request.url
        file_name = url.split('/')[-1]
        return file_name

    def item_completed(self, results, item, info):
        # 单个图片下载失败的处理: 这个官方写法
        # results代表下载的结果状态. x[path]为图片保存的相对路径,注意
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("图片下载失败")
        # item['image_paths'] = image_paths[0]  这会自动加一个image_paths.若item不存在,会报错
        return item
