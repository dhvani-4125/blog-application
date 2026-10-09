# Case study: THE WITHIN

*A fictional portfolio concept. No users, clients, revenue or outcomes are claimed.*

## The problem
Wellness practitioners (therapists, nutritionists, movement teachers) often get websites that look either clinical or generic. I wanted to show I can design and build something that feels like a considered brand while still being a working product.

## The concept
THE WITHIN is a small multidisciplinary practice with an editorial journal attached. The journal builds trust through useful, gentle writing; the practice pages turn that trust into an enquiry.

## My role
Everything: audit of the existing API, backend extension, content writing, UX, visual design, front-end build, testing and documentation.

## Tech stack
Django, Django REST Framework, SimpleJWT, PostgreSQL (SQLite for local tests), vanilla ES-module front end, hand-written CSS.

## Design direction
Warm ivory and espresso with clay, terracotta, olive and sage accents. Serif display type with a quiet sans. Arch-shaped crops and flat colour compositions. No gradients, no decorative effects.

## UX approach
- Navigation mirrors how people think about wellbeing (Mind, Body, Nourish, Ritual) rather than content types.
- "Find your starting point" lets a visitor say what they want in plain words and returns real stories plus a next step.
- Every list has loading, empty, error and end-of-results states with human copy.
- The contact form asks for as little as possible and says plainly that it is not for urgent concerns.

## Content strategy
26 original articles, written to be plain, specific and non-prescriptive: no statistics, no invented research, no diagnosis, with a gentle "speak to a professional" note where a topic touches health.

## Backend architecture
I extended the existing Django app instead of replacing it. Existing endpoints stayed intact; new ones were added for filtered listing, slug detail, related stories, likes, comments, contact and registration. Writes are limited to the author or staff.

## API
Page-number pagination, `category`, `q` and `featured` filters, correct status codes (200/201/204/400/401/403/404), throttling on public write endpoints.

## Database
Additive migration `0004` added editorial fields. Existing migrations were preserved.

## Authentication
JWT with refresh-once-on-401 handling in the client.

## Responsive design
Layouts are recomposed per breakpoint: the header collapses to a full-screen menu, the hero stacks image-first, category chips become a horizontal scroller, the story grid becomes a single column.

## Accessibility
Skip link, landmarks, labelled form controls with announced errors, visible focus, keyboard-accessible menu, reduced-motion support, descriptive alt text on meaningful images.

## Challenges and solutions
- **Migration drift.** The models file had lost three models that a migration still created; a naive `makemigrations` would have dropped them. I diagnosed it with a dry run, restored the models, and only then added a new migration.
- **No photography available.** I built a coherent set of flat-colour illustrations so the layout could be judged honestly, and documented how to swap in photos.
- **Secrets in settings.** Moved to environment variables, with an `.env.example`.

## Outcome
A working end-to-end site: API, seeded content, and a responsive front end, verified with automated API tests and a headless-browser run.

## What I learned
Auditing before building matters; the most valuable fix in this project was one nobody could see.

## Future improvements
Real photography, a bundler and component tests, cookie-based auth, prerendering for SEO, a moderation queue.
