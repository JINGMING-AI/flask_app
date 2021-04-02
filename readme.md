# 创建虚拟环境
`pip3 install virtualenv`

`python3 -m virtualenv venv`

# 激活虚拟环境
Mac     `source venv/bin/activate`
Windows `venv\scripts\activate`
# 安装依赖
`pip install`



# 项目结构
* app.py        项目文件
* db_config.py  数据库配置
* venv          虚拟环境
* utils         工具包
* models        数据模型
* operation     数据库操作
* api           数据接口实现
* handler       项目路由配置（数据接口/view界面）模块化 使用blueprint

##   app--handler--api--operation-models   ##



