"""Idempotent content seed for THE WITHIN. Safe to re-run: existing rows are never overwritten or deleted."""
from datetime import timedelta

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.utils.text import slugify

from blog.models import BlogPost, Category
from blog.seed_data import ARTICLES, CATEGORIES, EDITORS


class Command(BaseCommand):
    help = "Create the THE WITHIN categories, editors and articles (additive only)."

    def handle(self, *args, **options):
        cats = {}
        for name, slug, desc, tagline, order in CATEGORIES:
            cat, _ = Category.objects.get_or_create(
                name=name, defaults={'slug': slug, 'description': desc, 'tagline': tagline, 'display_order': order})
            if not cat.slug:
                cat.slug = slug
                cat.save()
            cats[slug] = cat

        editors = []
        for username, first, last in EDITORS:
            user, created = User.objects.get_or_create(
                username=username, defaults={'first_name': first, 'last_name': last})
            if created:
                user.set_unusable_password()
                user.save()
            editors.append(user)

        now = timezone.now()
        made = 0
        for title, cat_slug, editor, days_ago, featured, excerpt, alt, body in ARTICLES:
            slug = slugify(title)[:50].rstrip('-')
            if BlogPost.objects.filter(slug=slug).exists():
                continue
            BlogPost.objects.create(
                title=title, slug=slug, content=body.strip(), author=editors[editor],
                category=cats[cat_slug], status='published', excerpt=excerpt,
                hero_image=f'img/{slug}.svg', hero_image_alt=alt, is_featured=featured,
                published_at=now - timedelta(days=days_ago))
            made += 1
        self.stdout.write(self.style.SUCCESS(f'Seed complete: {made} new stories, {BlogPost.objects.count()} total.'))
