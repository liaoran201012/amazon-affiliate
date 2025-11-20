# 快速开始指南

## 第一步：填写产品数据

1. 打开 `data/products.csv` 文件（用Excel或文本编辑器打开）
2. 在表格中添加你的Amazon产品信息

### CSV表格格式示例：

```
id,name,category,amazon_url,price,image_url,description,rating,review_count,pros,cons,affiliate_link
1,iPhone 15 Pro,Electronics,https://amazon.com/iPhone,999,https://example.com/iphone.jpg,最新款苹果手机,4.8,1500,屏幕优秀;性能强劲;续航好,价格昂贵,https://amazon.com/iPhone?tag=youraffiliateID
2,MacBook Pro,Electronics,https://amazon.com/MacBook,1999,https://example.com/macbook.jpg,专业级笔记本,4.7,800,性能强;屏幕清晰,重量较重;价格高,https://amazon.com/MacBook?tag=youraffiliateID
```

### 字段说明：

| 字段 | 说明 | 示例 |
|------|------|------|
| id | 产品ID（唯一，建议用数字） | 1, 2, 3... |
| name | 产品名称 | iPhone 15 Pro |
| category | 产品分类 | Electronics, Home, Books |
| amazon_url | Amazon产品页面链接 | https://amazon.com/... |
| price | 产品价格 | 99.99 |
| image_url | 产品图片URL（必须是网络链接） | https://... |
| description | 产品描述 | 简短的产品介绍 |
| rating | 评分（0-5） | 4.5 |
| review_count | 评价数量 | 200 |
| pros | 优点（用分号;分隔多个） | 优点1;优点2;优点3 |
| cons | 缺点（用分号;分隔多个） | 缺点1;缺点2 |
| affiliate_link | Amazon联盟链接 | https://amazon.com/...?tag=YOUR_TAG |

**重要：将 `YOUR_TAG` 替换为你的Amazon联盟ID**

## 第二步：生成网页

1. 打开命令行/PowerShell
2. 进入项目目录：
   ```bash
   cd amazon-affiliate-site
   ```
3. 运行生成脚本：
   ```bash
   python scripts/generate_pages.py
   ```

你会看到类似的输出：
```
[OK] Generated: content/products/1-iphone-15-pro.md
[OK] Generated: content/products/2-macbook-pro.md
[SUCCESS] Successfully generated 2 product pages!
```

## 第三步：本地预览（可选）

在生成页面后，可以在本地预览：

```bash
hugo server --buildDrafts
```

然后打开浏览器访问：`http://localhost:1313`

按 `Ctrl+C` 停止本地服务器。

## 第四步：部署到GitHub

### 4.1 初始化Git仓库

```bash
git init
git add .
git commit -m "Initial commit: Amazon affiliate site"
git branch -M main
```

### 4.2 创建GitHub仓库

1. 登录到 [GitHub](https://github.com)
2. 点击右上角的 `+` 图标 → 选择 `New repository`
3. 仓库名：`amazon-affiliate` （或任何你喜欢的名字）
4. 选择 `Public`（因为需要GitHub Pages）
5. 点击 `Create repository`

### 4.3 推送代码到GitHub

复制新仓库的HTTPS地址，然后运行：

```bash
git remote add origin https://github.com/YOUR_USERNAME/amazon-affiliate.git
git push -u origin main
```

替换 `YOUR_USERNAME` 为你的GitHub用户名。

### 4.4 配置GitHub Pages

1. 进入GitHub仓库页面
2. 点击 `Settings` → `Pages`
3. 在 "Build and deployment" 中：
   - Source 选择 `GitHub Actions`
   - 系统会自动部署（使用我们已配置的 `.github/workflows/deploy.yml`）
4. 等待部署完成（通常2-3分钟）
5. 网站地址为：`https://YOUR_USERNAME.github.io/amazon-affiliate/`

## 后续更新产品

每次添加新产品或修改产品信息时：

1. 编辑 `data/products.csv`
2. 运行生成脚本：`python scripts/generate_pages.py`
3. 提交更改：
   ```bash
   git add .
   git commit -m "Update products"
   git push
   ```
4. GitHub会自动重新部署网站

## 自定义网站

### 修改网站标题和描述

编辑 `hugo.toml`：

```toml
title = '你的网站名称'

[params]
description = '你的网站描述'
author = '你的名字'
```

### 修改网站颜色和样式

编辑 `themes/affiliate-theme/static/css/style.css`

常见颜色修改点：
- 第7行：`#667eea` - 主题紫色
- 第8行：`#764ba2` - 深紫色
- 第88行：`#e74c3c` - 价格红色

### 修改页面布局

编辑以下文件：
- `themes/affiliate-theme/layouts/index.html` - 首页
- `themes/affiliate-theme/layouts/_default/single.html` - 产品详情页

## 常见问题

### Q: 图片URL怎么获取？

A: 在Amazon产品页面，右键点击产品图片 → 复制图片地址，粘贴到 `image_url` 字段。

### Q: 如何获取Amazon联盟ID？

A: 参考 [Amazon联盟帮助](https://affiliate-program.amazon.com/)

### Q: 生成脚本出错怎么办？

A: 检查：
- CSV文件是否有中文编码问题
- 字段数是否正确
- 没有多余的空格或特殊字符

### Q: 本地预览显示空白？

A: 确保运行过 `python scripts/generate_pages.py` 生成了页面文件。

### Q: GitHub Pages没有部署？

A: 检查：
- 仓库是否为Public
- 是否已推送到 `main` 分支
- GitHub Actions权限是否正确（Settings → Actions）

## 文件结构说明

```
amazon-affiliate-site/
├── .github/
│   └── workflows/
│       └── deploy.yml          ← GitHub自动部署配置
├── content/
│   └── products/               ← 自动生成的产品页面
├── data/
│   └── products.csv            ← 你填写的产品数据
├── scripts/
│   └── generate_pages.py       ← 生成脚本
├── themes/
│   └── affiliate-theme/        ← 网站主题
├── hugo.toml                   ← Hugo配置
└── README.md
```

## 需要帮助？

- 查看 `README.md` 了解完整文档
- 检查 `themes/affiliate-theme/` 中的HTML和CSS文件
- 参考 [Hugo官方文档](https://gohugo.io/)
