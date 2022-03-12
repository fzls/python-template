python示例模板

# 核心文件说明
## main.py
主要入口，可以在其中调用lib包中的定义的子模块或者子包

## lib
在这里面可以添加新的模块或者子包，参照 [Python 模块](https://docs.python.org/3/tutorial/modules.html)

# 其他文件说明
## .github
### dependabot.yml
用于自动提示升级版本，会在github上自动提交pr

### workflows
包含lint和test相关的workflow定义，会在github action中按配置自动执行

## .editorconfig
用于配置一些通用代码风格配置

## .gitignore
用于配置git忽略的文件

## .pre-commit-config.yaml
配置了flake8、isort、mypy等代码检查工具，目前用于在tox中触发lint

## .python-version
定义项目使用的python版本，如果修改为python3.10以外的版本，记得将tox.ini中的python版本也修改

## _build.bat
方便一键使用pyinstaller打包的脚本

## mypy.ini
用于配置mypy的代码检查工具

## requirements.txt
正常运行时的依赖库定义

## requirements_dev.txt
本地开发测试时需要的依赖库定义

## tox.ini
定义了使用tox运行测试和lint的配置，具体使用方式如下

```shell
# test
tox -e py310

# lint
tox -e lint

# all
tox
```
