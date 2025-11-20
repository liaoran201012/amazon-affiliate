# Amazon Affiliate Site

一个简洁高效的Amazon联盟推广网站，基于Hugo和自动化脚本，轻松管理产品数据。

## 项目结构

```
amazon-affiliate-site/
├── content/              # Hugo内容文件
│   └── products/        # 产品页面（自动生成）
├── data/
│   └── products.csv     # 产品数据表格（你需要填写）
├── scripts/
│   └── generate_pages.py # 自动生成页面脚本
├── themes/
│   └── affiliate-theme/  # 自定义主题
├── static/              # 静态文件（CSS、JS、图片）
└── hugo.toml           # Hugo配置文件
```

## 快速开始

### 1. 填写产品数据

打开 `data/products.csv` 文件，填写你的Amazon产品信息：

```csv
id,name,category,amazon_url,price,image_url,description,rating,review_count,pros,cons,affiliate_link
1,产品名称,电子产品,https://amazon.com/...,99.99,https://example.com/image.jpg,产品描述,4.5,200,优点1;优点2,缺点1;缺点2,https://amazon.com/...?tag=YOUR_TAG
```

**字段说明：**
- `id`: 产品ID（唯一）
- `name`: 产品名称
- `category`: 产品分类
- `amazon_url`: Amazon产品链接
- `price`: 价格
- `image_url`: 产品图片URL
- `description`: 产品描述
- `rating`: 评分（0-5）
- `review_count`: 评价数量
- `pros`: 优点（用分号分隔）
- `cons`: 缺点（用分号分隔）
- `affiliate_link`: Amazon联盟链接（替换YOUR_TAG为你的联盟ID）

### 2. 生成页面

运行Python脚本自动生成Hugo页面：

```bash
python scripts/generate_pages.py
```

这会在 `content/products/` 目录下自动生成Markdown文件。

### 3. 本地预览

```bash
hugo server --buildDrafts
```

访问 `http://localhost:1313` 查看网站。

### 4. 部署到GitHub Pages

1. 创建GitHub仓库：
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/amazon-affiliate.git
   git push -u origin main
   ```

2. 在GitHub仓库设置中：
   - 进入 `Settings` → `Pages`
   - 选择 `Deploy from a branch`
   - 选择分支 `main` 和目录 `/ (root)`
   - 或者设置 `GitHub Actions` 自动部署

3. 访问你的网站：
   ```
   https://YOUR_USERNAME.github.io/amazon-affiliate/
   ```

## 自定义网站

### 修改网站信息

编辑 `hugo.toml`：
```toml
baseURL = 'https://YOUR_USERNAME.github.io/amazon-affiliate/'
title = '你的网站名称'

[params]
description = '你的网站描述'
author = '你的名字'
```

### 修改主题样式

编辑 `themes/affiliate-theme/static/css/style.css` 修改颜色、布局等。

### 修改页面布局

编辑以下文件修改页面结构：
- `themes/affiliate-theme/layouts/index.html` - 首页
- `themes/affiliate-theme/layouts/_default/single.html` - 产品详情页

## 工作流程

1. **编辑产品数据** → 修改 `data/products.csv`
2. **生成页面** → 运行 `python scripts/generate_pages.py`
3. **本地测试** → 运行 `hugo server`
4. **推送到GitHub** → 自动部署到GitHub Pages

## 提示

- 确保 `affiliate_link` 包含你的Amazon联盟ID（tag=YOUR_AFFILIATE_TAG）
- 产品图片URL应该是外部链接（建议使用Amazon的产品图片URL）
- 定期更新产品信息和价格
- 首页会自动显示所有产品，无需额外配置

## 注意事项

- 遵守Amazon联盟计划的规则和政策
- 在网站上清楚地标示这是联盟链接
- 只推荐你真正使用过或相信的产品
- 定期检查和更新产品信息

## 许可证

MIT License
