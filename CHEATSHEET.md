# 快速参考卡 (Cheatsheet)

## 三行命令快速开始

```bash
# 1. 编辑产品数据
# 打开: data/products.csv

# 2. 生成网页
python scripts/generate_pages.py && hugo --minify

# 3. 上传GitHub
git add . && git commit -m "Update" && git push
```

## CSV数据快速模板

```csv
id,name,category,amazon_url,price,image_url,description,rating,review_count,pros,cons,affiliate_link
1,产品名,电子产品,https://amazon.com/product,99.99,https://image.jpg,描述,4.5,100,优点1;优点2,缺点1;缺点2,https://amazon.com/product?tag=ID
```

## 常用命令

| 命令 | 说明 |
|------|------|
| `python scripts/generate_pages.py` | 生成产品页面 |
| `hugo server --buildDrafts` | 本地预览（localhost:1313） |
| `hugo --minify` | 生成压缩的网站 |
| `hugo clean` | 清除缓存 |
| `git add .` | 提交所有更改 |
| `git commit -m "消息"` | 创建提交 |
| `git push` | 上传到GitHub |

## 网站修改位置

| 要修改 | 文件位置 |
|--------|---------|
| 网站标题 | `hugo.toml` 第3行 |
| 网站描述 | `hugo.toml` 第7行 |
| 产品颜色 | `themes/affiliate-theme/static/css/style.css` |
| 首页布局 | `themes/affiliate-theme/layouts/index.html` |
| 产品页布局 | `themes/affiliate-theme/layouts/_default/single.html` |
| 产品数据 | `data/products.csv` |

## CSV字段说明（简版）

| 字段 | 示例 |
|------|------|
| id | 1, 2, 3 |
| name | iPhone 15 Pro |
| category | Electronics |
| amazon_url | https://amazon.com/iPhone |
| price | 999 |
| image_url | https://m.media-amazon.com/... |
| description | Apple最新款手机 |
| rating | 4.8 |
| review_count | 2000 |
| pros | 屏幕好;性能强;续航好 |
| cons | 价格高;无配件 |
| affiliate_link | https://amazon.com/iPhone?tag=YOUR_TAG |

## GitHub部署快速指南

```bash
# 首次设置
git init
git add .
git commit -m "Initial"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/amazon-affiliate.git
git push -u origin main

# 之后每次更新
git add .
git commit -m "Update"
git push
```

## 颜色代码（用于CSS修改）

| 颜色 | 代码 |
|------|------|
| 紫色（当前） | `#667eea` |
| 深紫色（当前） | `#764ba2` |
| 红色（价格） | `#e74c3c` |
| 蓝色 | `#45B7D1` |
| 绿色 | `#2ecc71` |
| 橙色 | `#FFA07A` |
| 青色 | `#4ECDC4` |

## 常见错误排查

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| CSV解析错误 | 编码问题 | 用UTF-8编码保存 |
| 页面不显示 | 缺少CSS文件 | 运行 `hugo --minify` |
| GitHub部署失败 | 仓库设置 | 检查Settings→Pages |
| 图片不显示 | URL无效 | 检查image_url是否可访问 |
| 生成脚本报错 | Python编码 | 检查CSV格式是否正确 |

## 文件快速导航

```
📁 amazon-affiliate-site/
  📄 data/products.csv         ← 编辑产品数据
  📄 scripts/generate_pages.py ← 运行这个脚本
  📁 content/products/         ← 自动生成的页面
  📁 themes/affiliate-theme/   ← 网站主题文件
  📄 hugo.toml                 ← 网站配置
  📄 build.bat                 ← Windows构建
  📄 build.sh                  ← Mac/Linux构建
```

## 网址参考

| 内容 | URL |
|------|-----|
| 网站地址 | https://YOUR_USERNAME.github.io/amazon-affiliate/ |
| GitHub仓库 | https://github.com/YOUR_USERNAME/amazon-affiliate |
| GitHub设置 | https://github.com/YOUR_USERNAME/amazon-affiliate/settings |
| Hugo文档 | https://gohugo.io/ |
| Amazon联盟 | https://affiliate-program.amazon.com/ |

## 必须替换的地方

找到这些内容并替换为你的信息：

```
YOUR_USERNAME       → 你的GitHub用户名
YOUR_TAG           → 你的Amazon Associates ID
你的名字           → 你的真实名字
你的网站描述        → 你的网站描述
```

## 典型工作流程

```
1. 编辑 data/products.csv
2. 运行 python scripts/generate_pages.py
3. 本地测试 hugo server --buildDrafts
4. 上传 git add . && git commit && git push
5. 等待部署（2-3分钟）
6. 访问网站 https://YOUR_USERNAME.github.io/amazon-affiliate/
```

## 一键命令（复制粘贴）

### Windows (build.bat)
```bash
cd amazon-affiliate-site
build.bat
```

### Mac/Linux (build.sh)
```bash
cd amazon-affiliate-site
chmod +x build.sh
./build.sh
```

## 有用的链接

- 📖 [完整文档](README.md)
- 🚀 [快速开始](QUICK_START.md)
- 📝 [项目总结](PROJECT_SUMMARY.md)
- 🛠️ [搭建指南](../../SETUP_GUIDE.md)

---

**记住**: 编辑 → 生成 → 测试 → 提交 → 部署！
