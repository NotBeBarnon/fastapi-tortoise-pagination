这个是一个基于FastApi+tortoise-orm的查询集分页器

主要通过对QuerySet进行分页排序等进行操作，再对即将响应的数据进行序列化，相比较一些先序列化再分页的分页器，这个会更轻简快速。

一、介绍
该分页器主要分为三个块：Params、PagePydantic和pagination
####1. Params
   前端传的参数，包括page(页数)、size(页面大小)和order_by(排序字段，选传)
####2. PagePydantic
``` data: Sequence[T]   # 查询数据列表
    total: int          # 查询总数
    page: int
    size: int
    total_pages: int    # 总页数
    next: str           # 下页url
    previous: str       # 上页url
```
   响应模型，即返回给前端的数据模型
2. pagination
分页操作，将查询集QuerySet进行分页或者排序等操作，然后在根据用户自定义的Pydantic进行序列化，最后返回分页后的数据

二、快速开始：
1. install(安装)
    ```
    pip install fastapi-tortoise-pagination
    ```
2. 使用
 ```
     class ForumArticle(models.Model):
        """论坛文章"""
        id = fields.IntField(pk=True)
        user = fields.ForeignKeyField("cp_model.User", on_delete=fields.CASCADE)
        title = fields.CharField(max_length=32, default='', null=True)  # 文章标题
        content = fields.TextField(default='', null=True, blank=True)  # 文章正文

    class ForumArticleSchema(
    pydantic_model_creator(ForumArticle,
                           name="ForumArticleSchema",
                           exclude=())
    ):
    pass


    class TestViewSet(BaseViewSet):
        model = ForumArticle
        schema = ForumArticleSchema
        pk_type = str
        views = {
        }

    @Action.get("/list",  response_model=PagePydantic[ForumArticleSchema],description="分页获取帖子列表")  #
    async def list(self, params: Params = Depends()):
        query_set = ForumArticle.filter(is_delete=0)
        return await pagination(pydantic_model=ForumArticleSchema, query_set=query_set, params=params)
```

