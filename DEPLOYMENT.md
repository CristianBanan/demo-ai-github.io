# Deployment and Automation Guide

This guide covers the automated deployment and maintenance workflows for your Jekyll blog.

## 🚀 GitHub Actions Workflows

### 1. Build and Deploy (`build-and-deploy.yml`)

**Purpose**: Automatically builds and deploys your Jekyll blog to GitHub Pages

**Triggers**:
- Push to `main` branch (deploys)
- Pull requests (builds only)
- Weekly schedule (maintenance)

**Features**:
- ✅ **Ruby/Jekyll Setup**: Automated environment configuration
- ✅ **Dependency Caching**: Faster builds with gem caching
- ✅ **Content Validation**: Checks frontmatter and formatting
- ✅ **Build Testing**: Validates generated site structure
- ✅ **Artifact Upload**: Saves build for deployment
- ✅ **GitHub Pages Deploy**: Automatic deployment on main branch
- ✅ **Build Reports**: Detailed summary in GitHub Actions

**Workflow Steps**:
1. Checkout repository with full history
2. Setup Ruby 3.2 and install dependencies
3. Lint and validate content
4. Build Jekyll site with production settings
5. Test built site structure
6. Upload site artifact
7. Deploy to GitHub Pages (main branch only)
8. Generate deployment report

### 2. Content Quality Check (`content-quality.yml`)

**Purpose**: Ensures content quality and consistency

**Triggers**:
- Pull requests affecting posts or markdown files
- Manual workflow dispatch

**Features**:
- ✅ **New Post Detection**: Identifies added/modified posts
- ✅ **Frontmatter Validation**: Checks required fields
- ✅ **Content Analysis**: Word count and length checks
- ✅ **Link Validation**: Basic broken link detection
- ✅ **Statistics Generation**: Blog metrics and insights

**Quality Checks**:
- Required frontmatter fields (title, date)
- Optional fields (categories, tags, excerpt)
- Content length recommendations
- Link syntax validation

### 3. Scheduled Maintenance (`maintenance.yml`)

**Purpose**: Weekly maintenance and health monitoring

**Triggers**:
- Weekly schedule (Sundays at 2 AM UTC)
- Manual workflow dispatch

**Features**:
- ✅ **Dependency Updates**: Check for outdated gems
- ✅ **Content Analysis**: Missing metadata detection
- ✅ **Blog Analytics**: Posting trends and statistics
- ✅ **SEO Health Check**: Title length and meta descriptions
- ✅ **Performance Metrics**: Repository size and asset count

## 📋 Setup Instructions

### 1. Enable GitHub Pages

1. Go to repository **Settings** → **Pages**
2. Set source to **GitHub Actions**
3. Save configuration

### 2. Configure Repository Permissions

Ensure your repository has these permissions:
- **Actions**: Read and write permissions
- **Pages**: Write permissions
- **Metadata**: Read permissions

### 3. Environment Variables (Optional)

Add these secrets in **Settings** → **Secrets and variables** → **Actions**:

```bash
# For analytics integration
GOOGLE_ANALYTICS_ID=GA_MEASUREMENT_ID

# For advanced features
GITHUB_TOKEN=<automatically_provided>
```

## 🔧 Workflow Customization

### Modify Build Settings

Edit `.github/workflows/build-and-deploy.yml`:

```yaml
env:
  JEKYLL_ENV: production
  # Add custom environment variables
  CUSTOM_VAR: value
```

### Adjust Quality Checks

Customize content validation in `content-quality.yml`:

```yaml
# Modify word count thresholds
if [ "$WORD_COUNT" -lt 100 ]; then
  # Adjust minimum word count
```

### Change Maintenance Schedule

Update the cron schedule in `maintenance.yml`:

```yaml
schedule:
  # Run daily at midnight
  - cron: '0 0 * * *'
  # Run on first day of month
  - cron: '0 0 1 * *'
```

## 📊 Monitoring and Reports

### Build Status

Monitor deployment status:
- **Actions tab**: View workflow runs
- **Environments**: Check deployment history
- **Pages settings**: Verify site URL

### Quality Reports

Each workflow generates detailed reports:
- **Build Report**: Site size, page count, performance metrics
- **Quality Report**: Content validation results
- **Maintenance Report**: Dependency status, analytics

### Notifications

Set up notifications:
1. **Watch repository**: Get notified of workflow failures
2. **Email settings**: Configure GitHub notifications
3. **Slack integration**: Add webhook for team notifications

## 🚨 Troubleshooting

### Common Issues

**Build Failures**:
```bash
# Check Ruby/Jekyll versions
ruby --version
bundle exec jekyll --version

# Validate dependencies
bundle install
bundle exec jekyll build --verbose
```

**Deployment Issues**:
- Verify GitHub Pages is enabled
- Check repository permissions
- Ensure `GITHUB_TOKEN` has correct permissions

**Content Validation Errors**:
- Check YAML frontmatter syntax
- Verify required fields are present
- Validate markdown formatting

### Debug Mode

Enable debug output in workflows:

```yaml
- name: Debug build
  run: |
    bundle exec jekyll build --verbose --trace
  env:
    JEKYLL_LOG_LEVEL: debug
```

## 🎯 Best Practices

### Content Workflow

1. **Create feature branch** for new posts
2. **Use pull requests** to trigger quality checks
3. **Review quality report** before merging
4. **Merge to main** for automatic deployment

### Performance Optimization

- **Optimize images** before committing
- **Minimize asset sizes** for faster loading
- **Use Jekyll plugins** efficiently
- **Monitor build times** in workflow reports

### Security

- **Keep dependencies updated** via maintenance workflow
- **Review third-party actions** before using
- **Use secrets** for sensitive configuration
- **Enable branch protection** rules

## 📈 Advanced Features

### Custom Deployment Targets

Deploy to multiple environments:

```yaml
# Add staging environment
staging:
  if: github.ref == 'refs/heads/develop'
  environment:
    name: staging
    url: https://staging.example.com
```

### Integration with External Services

Add external integrations:

```yaml
- name: Notify external service
  run: |
    curl -X POST https://api.service.com/webhook \
         -H "Authorization: Bearer ${{ secrets.API_TOKEN }}" \
         -d '{"status":"deployed","url":"${{ steps.deployment.outputs.page_url }}"}'
```

### Performance Testing

Add performance audits:

```yaml
- name: Performance audit
  run: |
    npm install -g lighthouse
    lighthouse ${{ steps.deployment.outputs.page_url }} --output=json --output-path=./lighthouse-report.json
```

---

**🎉 Your blog is now fully automated!** Every push to main will trigger a complete build, test, and deployment cycle, ensuring your content is always live and optimized.

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Jekyll CI/CD Guide](https://jekyllrb.com/docs/continuous-integration/)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)