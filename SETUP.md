# GitHub Repository Configuration

## Required Repository Settings

To enable automated deployment and GitHub Pages, configure these settings:

### 1. GitHub Pages Configuration

**Location**: Repository Settings → Pages

```
Source: GitHub Actions
Custom domain: (optional)
Enforce HTTPS: ✅ Enabled
```

### 2. Actions Permissions

**Location**: Repository Settings → Actions → General

```
Actions permissions: Allow all actions and reusable workflows
Workflow permissions: Read and write permissions
Allow GitHub Actions to create and approve pull requests: ✅ Enabled
```

### 3. Environment Protection (Optional)

**Location**: Repository Settings → Environments

Create `github-pages` environment with:
```
Deployment branches: Selected branches (main)
Environment secrets: (none required)
Protection rules: (optional)
```

## 🔧 Manual Setup Commands

If you prefer to set up locally before pushing:

```bash
# Clone and navigate to repository
git clone https://github.com/CristianBanan/demo-ai-github.io.git
cd demo-ai-github.io

# Install Ruby dependencies
bundle install

# Test build locally
bundle exec jekyll serve

# Create and test new post
python new_post.py -i

# Commit and push changes
git add .
git commit -m "Add automated deployment workflows"
git push origin main
```

## 📋 Pre-deployment Checklist

Before your first deployment:

- [ ] Repository is public or has GitHub Pages enabled
- [ ] Actions are enabled in repository settings
- [ ] Main branch protection rules configured (optional)
- [ ] Custom domain configured (if using)
- [ ] Analytics tracking ID added (if using)
- [ ] Social media links updated in `_config.yml`
- [ ] About page content customized
- [ ] First blog post created and reviewed

## 🚀 Deployment Verification

After pushing to main, verify:

1. **Actions tab**: Build workflow completes successfully
2. **Environments**: Deployment shows as active
3. **Settings → Pages**: Shows deployment URL
4. **Live site**: Accessible at GitHub Pages URL

Your blog will be available at:
`https://cristianbanan.github.io/demo-ai-github.io`

## 🔄 Ongoing Maintenance

The automated workflows will handle:
- Weekly dependency checks
- Content quality validation
- Performance monitoring
- SEO health checks
- Build optimization

Manual tasks:
- Review and merge pull requests
- Update content regularly
- Monitor analytics
- Respond to workflow notifications