# Demo AI GitHub Pages Blog

A Jekyll-based blog demonstrating GitHub Pages capabilities for AI and technology content.

## 🚀 Live Site

Visit the blog at: [https://cristianbanan.github.io/demo-ai-github.io](https://cristianbanan.github.io/demo-ai-github.io)

## 📁 Project Structure

```
├── _config.yml          # Jekyll configuration
├── _posts/              # Blog posts directory
├── _layouts/            # Custom layouts
├── index.md             # Home page
├── about.md             # About page
├── Gemfile              # Ruby dependencies
└── README.md            # This file
```

## 🛠️ Local Development

To run this site locally:

1. **Install Ruby and Bundler**
   ```bash
   # Install dependencies
   bundle install
   ```

2. **Run Jekyll locally**
   ```bash
   bundle exec jekyll serve
   ```

3. **View the site**
   - Open http://localhost:4000 in your browser
   - The site will auto-reload when you make changes

## 📝 Adding New Posts

1. Create a new file in `_posts/` directory
2. Name it: `YYYY-MM-DD-title.md`
3. Add front matter:
   ```yaml
   ---
   layout: post
   title: "Your Post Title"
   date: 2025-09-30 12:00:00 +0000
   categories: category1 category2
   tags: [tag1, tag2, tag3]
   author: Your Name
   ---
   ```
4. Write your content in Markdown

## ⚙️ Configuration

Main configuration is in `_config.yml`. Key settings:
- Site title and description
- Social media links
- Theme settings
- Plugin configuration

## 🎨 Customization

- **Layouts**: Modify files in `_layouts/`
- **Styling**: Add custom CSS to assets or layouts
- **Plugins**: Add to `_config.yml` and `Gemfile`

## 📦 Dependencies

- Jekyll (static site generator)
- Minima theme (default GitHub Pages theme)
- Jekyll plugins for SEO, feeds, and sitemap

## 🔧 GitHub Pages Setup

This site is configured for GitHub Pages with:
- Automatic building and deployment
- Custom domain support ready
- SEO optimization
- RSS feed generation

## 📄 License

This project is open source and available under the [MIT License](LICENSE).