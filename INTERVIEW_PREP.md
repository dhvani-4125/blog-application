# Interview preparation: THE WITHIN
Everything below reflects what is actually implemented.

**1. 30 seconds.** THE WITHIN is a fictional wellness practice with an editorial journal. I extended an existing Django REST blog API and built a responsive front end with search, category filtering, pagination, article pages, likes, notes, a contact form and an interactive starting-point feature.

**2. 1 minute.** I inherited a backend-only blog API. I audited it, found a model/migration mismatch that would have deleted data, fixed it safely, added an additive migration, and extended the API. I wrote 26 original articles, built a dependency-free front end that reads everything from the API, and tested the API with Django tests and the UI in headless Chrome.

**3. Why this concept.** Wellness practitioners are a realistic client group, and the brand needs warmth and trust, which makes design and writing decisions visible.

**4. Why the UX looks this way.** Editorial layout signals care and calm; navigation uses plain-language categories; the starting-point feature lets visitors begin without knowing the right service name.

**5. Front-end architecture.** One ES module with a small history-API router, an API client with token refresh, string-template views with an `esc()` helper for all API data, and CSS custom properties. No build step.

**6. Backend architecture.** Existing app kept; new class-based views and serializers added; permissions limit writes to authors/staff; queries use `select_related` and annotated counts.

**7. API.** REST, JWT bearer auth, filters via query params, paginated lists, proper status codes, throttled public writes.

**8. Database.** Category, BlogPost, Comment, Like (unique per user/post), Feedback. Migration 0004 added editorial fields without touching earlier migrations.

**9. Authentication.** SimpleJWT; registration validates passwords; the client refreshes once on a 401 then signs out. Tokens are in localStorage, which I would replace with httpOnly cookies for sensitive data.

**10. CRUD.** Posts can be created, read, updated and deleted through the API (author or staff only); comments can be created and deleted; likes toggle. Content is also editable in Django admin.

**11. Pagination.** DRF page-number pagination (9 per page); the UI handles first, middle, last and out-of-range pages and shows the end of results.

**12. Search.** Server-side `icontains` across title, excerpt, body and category name, with loading, no-results, error and clear states. It is simple database search, not a ranked search engine.

**13. Category filtering.** Categories come from the API; filtering by slug is server-side; category pages have their own URLs.

**14. Comments, likes, feedback.** Likes and notes require sign-in and are validated (2–1000 characters); owners and staff can delete; admin can moderate. Contact submissions are stored as Feedback.

**15. Responsive design.** Layouts are recomposed at breakpoints; verified with no horizontal overflow at mobile, tablet and desktop widths.

**16. Accessibility.** Skip link, landmarks, labelled inputs with announced errors, focus styles, keyboard menu, reduced-motion handling. I have not run a full screen-reader audit.

**17. Biggest technical challenge.** Making further changes safely when the models file disagreed with migration history.

**18. Biggest design challenge.** Building a coherent image system without photography access; I used flat-colour illustrations and kept the layout ready for real photos.

**19. Biggest bug.** `makemigrations` wanted to delete Feedback, Comment and Like because the models had been removed from `models.py`.

**20. How I solved it.** Ran a dry run to see the plan, restored the models to match migration 0003, confirmed "No changes detected", then created a new additive migration.

**21. What I would improve.** Real photography, a bundler and component tests, cookie auth, prerendering for SEO, CI against PostgreSQL, a moderation queue.

**22. Relevance to a wellness web-design company.** It shows tone-appropriate design, careful non-clinical copy, a form that avoids collecting sensitive data, and an editorial content system practitioners could actually maintain through the admin.
