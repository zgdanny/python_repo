import pkgutil
import fnmatch

# 获取当前Python环境中所有可用的模块
modules = list(pkgutil.iter_modules())

# 获取用户输入的模块名
module_name = input("请输入要搜索的模块名称：")

# 使用模糊匹配查找模块
matched_modules = []
for module in modules:
    if fnmatch.fnmatch(module.name, f"*{module_name}*"):
        matched_modules.append(module.name)

# 打印匹配的模块名称
if matched_modules:
    print("匹配的模块如下：")
    for module in matched_modules:
        print(module)
else:
    print("没有找到匹配的模块。")
