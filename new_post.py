#!/usr/bin/env python3
# new_post.py
# Script to generate Jekyll blog post templates

import datetime
import sys
import os
import re
import argparse

def create_post(title, categories=None, tags=None, excerpt=""):
    """Generate a new blog post with frontmatter."""
    date = datetime.datetime.now()
    
    # Create URL-friendly filename
    slug = title.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)  # Remove special characters
    slug = re.sub(r'[-\s]+', '-', slug)   # Replace spaces and multiple dashes
    slug = slug.strip('-')                 # Remove leading/trailing dashes
    
    filename = f"_posts/{date.strftime('%Y-%m-%d')}-{slug}.md"
    
    # Ensure _posts directory exists
    os.makedirs('_posts', exist_ok=True)
    
    # Format categories and tags
    categories_str = format_yaml_list(categories) if categories else "[]"
    tags_str = format_yaml_list(tags) if tags else "[]"
    
    # Generate frontmatter template
    frontmatter = f"""---
layout: post
title: "{title}"
date: {date.strftime('%Y-%m-%d %H:%M:%S')} +0000
categories: {categories_str}
tags: {tags_str}
author: "CristianBanan"
excerpt: "{excerpt}"
---

# {title}

## Introduction

[Write your introduction here. Explain what this post is about and why it matters to your readers.]

## Main Content

### Key Points

1. **First Point**: [Develop your first main idea]
2. **Second Point**: [Develop your second main idea]
3. **Third Point**: [Develop your third main idea]

### Code Example (if applicable)

```python
# Add relevant code examples
def example_function():
    print("Hello, World!")
    return "success"
```

### Visual Elements

- Add images with: `![Alt text](path/to/image.jpg)`
- Create lists for better readability
- Use blockquotes for important information

> **Tip**: Remember to optimize your content for both readers and search engines.

## Implementation Details

[If this is a technical post, provide step-by-step implementation details]

1. Step one
2. Step two
3. Step three

## Best Practices

- Practice one
- Practice two
- Practice three

## Conclusion

[Wrap up your post by summarizing key takeaways and providing next steps for readers]

### What's Next?

- Link to related posts
- Suggest further reading
- Encourage reader engagement

---

*What are your thoughts on this topic? Feel free to share your experiences in the comments below!*
"""
    
    # Check if file already exists
    if os.path.exists(filename):
        print(f"❌ Error: Post '{filename}' already exists!")
        return False
    
    # Write the file
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(frontmatter)
        print(f"✅ Successfully created new post: {filename}")
        print(f"📝 Title: {title}")
        print(f"📅 Date: {date.strftime('%Y-%m-%d %H:%M:%S')}")
        if categories:
            print(f"📁 Categories: {', '.join(categories)}")
        if tags:
            print(f"🏷️  Tags: {', '.join(tags)}")
        return True
    except Exception as e:
        print(f"❌ Error creating post: {e}")
        return False

def format_yaml_list(items):
    """Format a list for YAML frontmatter."""
    if not items:
        return "[]"
    if len(items) == 1:
        return f"[{items[0]}]"
    return "[" + ", ".join(items) + "]"

def list_recent_posts(limit=10):
    """List recent blog posts."""
    posts_dir = "_posts"
    if not os.path.exists(posts_dir):
        print("📂 No _posts directory found!")
        return
    
    posts = []
    for filename in os.listdir(posts_dir):
        if filename.endswith('.md') or filename.endswith('.markdown'):
            filepath = os.path.join(posts_dir, filename)
            mtime = os.path.getmtime(filepath)
            posts.append((filename, mtime))
    
    posts.sort(key=lambda x: x[1], reverse=True)
    
    print(f"📚 Recent Posts (last {min(limit, len(posts))}):")
    print("-" * 50)
    for i, (filename, mtime) in enumerate(posts[:limit]):
        date_str = datetime.datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M')
        print(f"{i+1:2}. {filename} (modified: {date_str})")

def interactive_mode():
    """Interactive mode for creating posts."""
    print("🚀 Jekyll Post Generator - Interactive Mode")
    print("=" * 45)
    
    title = input("📝 Enter post title: ").strip()
    if not title:
        print("❌ Title cannot be empty!")
        return False
    
    categories_input = input("📁 Enter categories (comma-separated, optional): ").strip()
    categories = [cat.strip() for cat in categories_input.split(',') if cat.strip()] if categories_input else None
    
    tags_input = input("🏷️  Enter tags (comma-separated, optional): ").strip()
    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()] if tags_input else None
    
    excerpt = input("📄 Enter excerpt (optional): ").strip()
    
    print("\n📋 Post Summary:")
    print(f"   Title: {title}")
    print(f"   Categories: {', '.join(categories) if categories else 'None'}")
    print(f"   Tags: {', '.join(tags) if tags else 'None'}")
    print(f"   Excerpt: {excerpt if excerpt else 'None'}")
    
    confirm = input("\n✅ Create this post? (y/N): ").strip().lower()
    if confirm in ['y', 'yes']:
        return create_post(title, categories, tags, excerpt)
    else:
        print("❌ Post creation cancelled.")
        return False

def main():
    parser = argparse.ArgumentParser(description='Generate Jekyll blog post templates')
    parser.add_argument('title', nargs='?', help='Post title')
    parser.add_argument('-c', '--categories', help='Comma-separated categories')
    parser.add_argument('-t', '--tags', help='Comma-separated tags')
    parser.add_argument('-e', '--excerpt', help='Post excerpt')
    parser.add_argument('-i', '--interactive', action='store_true', help='Interactive mode')
    parser.add_argument('-l', '--list', type=int, nargs='?', const=10, help='List recent posts')
    
    args = parser.parse_args()
    
    # List recent posts
    if args.list is not None:
        list_recent_posts(args.list)
        return
    
    # Interactive mode
    if args.interactive or not args.title:
        interactive_mode()
        return
    
    # Command line mode
    categories = [cat.strip() for cat in args.categories.split(',') if cat.strip()] if args.categories else None
    tags = [tag.strip() for tag in args.tags.split(',') if tag.strip()] if args.tags else None
    
    create_post(args.title, categories, tags, args.excerpt or "")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)