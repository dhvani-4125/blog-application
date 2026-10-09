/* THE WITHIN: dependency-free single-page front end for the Django API. */
const API = document.querySelector('meta[name="api-base"]').content.replace(/\/$/, '');
const main = document.getElementById('main');
const SITE = 'THE WITHIN';
const PAGE_SIZE = 9;

/* ---------- helpers ---------- */
const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const fmtDate = (iso) => (iso ? new Date(iso).toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }) : '');
const img = (p) => '/' + String(p || 'img/hero.svg').replace(/^\//, '');
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];

function setMeta(title, desc, image) {
  document.title = title ? `${title} | ${SITE}` : `${SITE} | A more considered way to care for yourself`;
  const d = desc || 'THE WITHIN is a fictional wellness practice and editorial journal exploring mind, body, nourishment and everyday ritual.';
  $('meta[name="description"]').content = d;
  $('meta[property="og:title"]').content = title || SITE;
  $('meta[property="og:description"]').content = d;
  let og = $('meta[property="og:image"]');
  if (!og) { og = document.createElement('meta'); og.setAttribute('property', 'og:image'); document.head.appendChild(og); }
  og.content = location.origin + img(image);
  const ld = $('#ld'); if (ld) ld.remove();
}

/* ---------- auth + api ---------- */
const Auth = {
  get access() { return localStorage.getItem('tw_access'); },
  get refresh() { return localStorage.getItem('tw_refresh'); },
  get name() { return localStorage.getItem('tw_name'); },
  set(a, r, n) { localStorage.setItem('tw_access', a); if (r) localStorage.setItem('tw_refresh', r); if (n) localStorage.setItem('tw_name', n); },
  clear() { ['tw_access', 'tw_refresh', 'tw_name'].forEach((k) => localStorage.removeItem(k)); },
};

class ApiError extends Error {
  constructor(status, data) { super(data?.detail || 'Request failed'); this.status = status; this.data = data || {}; }
}

async function raw(path, { method = 'GET', body, token } = {}) {
  const headers = {};
  if (body) headers['Content-Type'] = 'application/json';
  if (token) headers.Authorization = 'Bearer ' + token;
  const res = await fetch(API + path, { method, headers, body: body ? JSON.stringify(body) : undefined });
  const data = res.status === 204 ? null : await res.json().catch(() => ({}));
  if (!res.ok) throw new ApiError(res.status, data);
  return data;
}

async function api(path, opts = {}) {
  try {
    return await raw(path, { ...opts, token: Auth.access });
  } catch (e) {
    if (e.status === 401 && Auth.access) {
      if (Auth.refresh) {
        try {
          const t = await raw('/token/refresh/', { method: 'POST', body: { refresh: Auth.refresh } });
          Auth.set(t.access, t.refresh);
          return await raw(path, { ...opts, token: Auth.access });
        } catch { /* fall through */ }
      }
      Auth.clear(); renderAccount();
      if (opts.method && opts.method !== 'GET') throw e;
      return raw(path, opts);
    }
    throw e;
  }
}

function renderAccount() {
  const html = Auth.access
    ? `<span class="label">Hello, ${esc(Auth.name || 'reader')}</span> <button type="button" data-signout>Sign out</button>`
    : `<a href="/login" data-link>Sign in</a>`;
  $('#account-slot').innerHTML = html;
  $('#account-slot-mobile').innerHTML = html;
}

/* ---------- reference content ---------- */
const CATS = [
  { slug: 'mind', name: 'Mind', copy: 'Emotional wellbeing, relationships, self-awareness and reflection.' },
  { slug: 'body', name: 'Body', copy: 'Movement, mobility, strength, recovery and rest.' },
  { slug: 'nourish', name: 'Nourish', copy: 'Nutrition, mindful eating and our relationship with food.' },
  { slug: 'ritual', name: 'Ritual', copy: 'Mindfulness, meditation, journaling, spirituality and everyday rituals.' },
];
let categoryCache = null;
async function getCategories() {
  if (categoryCache) return categoryCache;
  try { categoryCache = await api('/categories/'); } catch { categoryCache = ['Mind', 'Body', 'Nourish', 'Ritual', 'Relationships', 'Rest'].map((n) => ({ name: n, slug: n.toLowerCase(), tagline: '' })); }
  return categoryCache;
}

const SERVICES = [
  { id: 'therapy', name: 'Therapy', title: 'Individual Therapy', img: 'svc-therapy', topic: 'Therapy',
    short: 'A private, unhurried space to talk things through with someone who listens first.',
    long: 'Sessions are shaped around what you bring: a transition, a relationship, a feeling you cannot quite name. We begin with a conversation about what you would like from the time, and go from there at your pace.' },
  { id: 'nutrition', name: 'Nutrition', title: 'Nutrition', img: 'svc-nutrition', topic: 'Nutrition',
    short: 'Practical, judgement-free conversations about food, routine and enjoyment.',
    long: 'We look at how you eat now, what you enjoy and what gets in the way, then build small, realistic changes together. There are no rigid plans and no food rules for their own sake.' },
  { id: 'movement', name: 'Movement', title: 'Movement', img: 'svc-movement', topic: 'Movement',
    short: 'Gentle strength, mobility and walking-based sessions for real bodies and real schedules.',
    long: 'Whether you are returning to movement or looking for variety, sessions are paced to how you feel on the day. The aim is confidence in your body and something you can keep doing.' },
  { id: 'mindfulness', name: 'Mindfulness', title: 'Mindfulness', img: 'svc-mindfulness', topic: 'Mindfulness',
    short: 'Short, practical attention practices that fit around an ordinary day.',
    long: 'Small group and one-to-one sessions explore breathing, noticing and simple daily practices. You leave with a few things you can use on a Tuesday afternoon, not an hour of homework.' },
  { id: 'consultation', name: 'Wellness Consultation', title: 'Wellness Consultation', img: 'svc-consultation', topic: 'Wellness consultation',
    short: 'A first conversation to work out where to begin and who might be the right fit.',
    long: 'Not sure which door to knock on? A consultation is an hour to talk through what is going on in your life and what you would like to feel differently, then decide on next steps together.' },
];

const PEOPLE = [
  { name: 'Tomas Reyes', role: 'Therapist', img: 'person-p1', focus: 'Life transitions, relationships, reflective conversation',
    approach: 'Warm, curious and unhurried. Starts with listening and lets the work set its own pace.',
    bio: 'Tomas believes most people already know a good deal about what they need and mostly want company while they work it out.' },
  { name: 'Wren Aldridge', role: 'Nutritionist', img: 'person-p2', focus: 'Everyday eating, cooking confidence, food and mood',
    approach: 'Practical and kind. Small changes, shared meals and no moral labels on food.',
    bio: 'Wren is happiest in a kitchen and tends to start sessions by asking what you had for breakfast and whether you enjoyed it.' },
  { name: 'Noor Haddad', role: 'Movement Specialist', img: 'person-p3', focus: 'Gentle strength, mobility, returning to movement',
    approach: 'Paced to how you feel that day. Strength is treated as a form of self-care, not a performance.',
    bio: 'Noor teaches movement the way some people teach languages: in short, regular sessions that make it feel familiar.' },
  { name: 'Esme Larkin', role: 'Mindfulness Practitioner', img: 'person-p4', focus: 'Attention practices, rest, daily rituals',
    approach: 'Plain language and short practices. Nothing esoteric required.',
    bio: 'Esme works with people who have tried meditation and decided they are bad at it, and gently suggests otherwise.' },
];

const STARTS = [
  { id: 'calm', label: 'I want to feel calmer.', cats: ['mind', 'ritual'], note: 'Start with quiet reflection and a few small rituals.', links: [['Explore Mind', '/category/mind'], ['Explore Ritual', '/category/ritual']] },
  { id: 'move', label: 'I want to move more.', cats: ['body'], note: 'Gentle, realistic ways to begin and to keep going.', links: [['Explore Body', '/category/body'], ['Movement sessions', '/practice#movement']] },
  { id: 'food', label: 'I want to understand my relationship with food.', cats: ['nourish'], note: 'Thoughts on eating, cooking and what food means to us.', links: [['Explore Nourish', '/category/nourish'], ['Nutrition sessions', '/practice#nutrition']] },
  { id: 'rituals', label: 'I want better daily rituals.', cats: ['ritual', 'rest'], note: 'Small, repeatable things that fit a full week.', links: [['Explore Ritual', '/category/ritual'], ['Explore Rest', '/category/rest']] },
  { id: 'therapy', label: "I'm thinking about therapy.", cats: ['mind', 'relationships'], note: 'Reading can help you find words for it. When you are ready, a first conversation is open to you.', links: [['About therapy here', '/practice#therapy'], ['Ask a question', '/contact?topic=Therapy']] },
];

/* ---------- shared fragments ---------- */
const arrow = '<span aria-hidden="true">→</span>';
const metaLine = (p) => `<span class="meta">${esc(p.category?.name || '')}<span class="dot" aria-hidden="true">·</span>${p.reading_time || 1} min read</span>`;

function storyCard(p, size = '') {
  return `<a class="story ${size} rv" href="/journal/${esc(p.slug)}" data-link>
    <div class="ph"><img src="${img(p.hero_image)}" alt="" width="1600" height="1000" loading="lazy"></div>
    <span class="label">${esc(p.category?.name)}</span>
    <h3>${esc(p.title)}</h3>
    <p class="ex">${esc(p.excerpt)}</p>
    ${size === 'lg' ? `<span class="meta">${esc(p.author)}<span class="dot" aria-hidden="true">·</span>${p.reading_time} min read</span>` : ''}
  </a>`;
}
const statusBox = (title, text, action = '') => `<div class="status" role="status"><h2>${esc(title)}</h2><p>${esc(text)}</p>${action}</div>`;
const errBox = (retryAttr = 'data-retry') => statusBox('Something went wrong.', "We couldn't reach the journal just now. Please try again in a moment.", `<button class="btn btn-line" type="button" ${retryAttr}>Try again</button>`);
const skeleton = () => '<div class="skel" aria-hidden="true"><i></i><i></i><i></i></div><p class="sr" role="status">Loading stories</p>';

/* ---------- pages ---------- */
async function home() {
  setMeta('', '', 'img/hero.svg');
  main.innerHTML = `
  <section class="hero" aria-labelledby="hero-h">
    <div class="hero-copy">
      <span class="label eyebrow">A more considered way to care for yourself</span>
      <h1 id="hero-h" class="h-xl">A softer way<br>to <em>live well.</em></h1>
      <p class="lede">Thoughtful perspectives on movement, nourishment, mental wellbeing and the rituals that help us feel more like ourselves.</p>
      <div class="row"><a class="btn btn-solid" href="/journal" data-link>Explore the journal</a><a class="btn btn-line" href="/practice" data-link>Meet the practice</a></div>
    </div>
    <div class="hero-img"><img src="/img/hero.svg" alt="Soft morning light over a quiet room" width="1600" height="1000" fetchpriority="high"></div>
  </section>

  <section class="sec" aria-labelledby="intro-h"><div class="wrap intro">
    <div class="rv"><span class="label eyebrow">Introduction</span><h2 id="intro-h" class="h-lg">Care, in all<br>its <em>forms.</em></h2></div>
    <div class="copy rv"><p>Feeling well is rarely about one thing. It is the night you slept properly, the conversation you finally had, the meal you made yourself, the walk that cleared your head. It is also the harder days, and what we do with them.</p><p>THE WITHIN brings together a journal and a small practice, because we think the reading and the doing belong together. Read a little. Try something small. Ask for help when it would be useful.</p></div>
  </div></section>

  <section class="sec" style="padding-top:0" aria-labelledby="explore-h"><div class="wrap">
    <div class="sec-head"><div><span class="label eyebrow">Explore your within</span><h2 id="explore-h" class="h-lg">Four places <em>to begin.</em></h2></div></div>
    <div class="cats">${CATS.map((c) => `<a class="cat rv" href="/category/${c.slug}" data-link>
      <div class="ph"><img src="/img/cat-${c.slug}.svg" alt="" width="1600" height="1000" loading="lazy"></div>
      <h3>${c.name} <span aria-hidden="true">→</span></h3><p>${c.copy}</p></a>`).join('')}</div>
  </div></section>

  <section class="feature" aria-labelledby="feat-h"><div class="feat-grid" id="feature-slot">
    <div class="feat-copy"><span class="label">Featured story</span><h2 id="feat-h" class="h-lg">Why rest doesn't always feel restful</h2><p class="ex">${skeletonLine()}</p></div>
  </div></section>

  <section class="sec" aria-labelledby="prac-h"><div class="wrap">
    <div class="sec-head"><div><span class="label eyebrow">The practice</span><h2 id="prac-h" class="h-lg">A small practice,<br><em>many kinds of care.</em></h2></div><p class="lede">A fictional multidisciplinary practice. Our services are conversations and guided sessions for general wellbeing, not treatments for medical conditions.</p></div>
    <div class="services">${SERVICES.map((s) => `<article class="svc rv"><div class="ph"><img src="/img/${s.img}.svg" alt="" width="1600" height="1000" loading="lazy"></div><span class="label">0${SERVICES.indexOf(s) + 1}</span><h3>${s.name}</h3><p>${s.short}</p><a class="tlink" href="/practice#${s.id}" data-link>Learn more</a></article>`).join('')}</div>
  </div></section>

  <section class="statement sec" aria-labelledby="stmt-h"><div class="wrap inner">
    <div class="rv"><h2 id="stmt-h" class="h-xl">Wellbeing is not <em>one-size-fits-all.</em></h2><p class="body" style="margin-top:28px">What steadies one person unsettles another. A quiet weekend is bliss for some and a struggle for others. We try to offer ideas and not instructions, and to leave room for you to decide what fits your own life.</p></div>
    <div class="arch rv"><img src="/img/about.svg" alt="A calm interior with warm tones" width="1600" height="1000" loading="lazy"></div>
  </div></section>

  <section class="sec" aria-labelledby="latest-h"><div class="wrap">
    <div class="sec-head"><div><span class="label eyebrow">Latest stories</span><h2 id="latest-h" class="h-lg">From the <em>journal.</em></h2></div><a class="tlink" href="/journal" data-link>All stories</a></div>
    <div id="latest">${skeleton()}</div>
  </div></section>

  <section class="start sec" aria-labelledby="start-h"><div class="wrap start-grid">
    <div><span class="label eyebrow">Find your starting point</span><h2 id="start-h" class="h-lg">What are you looking for <em>right now?</em></h2>
      <div class="opts" role="group" aria-label="Choose what you are looking for" style="margin-top:34px">${STARTS.map((s) => `<button class="opt" type="button" data-start="${s.id}" aria-pressed="false">${esc(s.label)}</button>`).join('')}</div></div>
    <div class="result" id="start-result" aria-live="polite"><p class="empty">Choose a statement on the left. We'll suggest where to read next.</p></div>
  </div></section>

  <section class="final sec" aria-labelledby="final-h"><div class="wrap">
    <h2 id="final-h" class="h-xl">You can start<br>with a <em>question.</em></h2>
    <p class="lede">You don't need to know exactly what you need before reaching out.</p>
    <a class="btn btn-light" href="/practice" data-link>Explore the practice</a>
  </div></section>`;

  loadHome();
  $$('[data-start]').forEach((b) => b.addEventListener('click', () => pickStart(b.dataset.start)));
}
const skeletonLine = () => 'Loading the story…';

async function loadHome() {
  const feat = $('#feature-slot'), latest = $('#latest');
  try {
    const [f, l] = await Promise.all([api('/posts/?featured=true&page_size=1'), api('/posts/?page_size=6')]);
    const p = f.results[0];
    if (p) {
      feat.innerHTML = `<div class="rv in"><img src="${img(p.hero_image)}" alt="${esc(p.hero_image_alt)}" width="1600" height="1000"></div>
        <div class="feat-copy"><span class="label">Featured story · ${esc(p.category.name)}</span><h2 id="feat-h" class="h-lg">${esc(p.title)}</h2><p class="ex">${esc(p.excerpt)}</p>
        <span class="meta">${esc(p.author)}<span class="dot" aria-hidden="true">·</span>${fmtDate(p.published_at)}<span class="dot" aria-hidden="true">·</span>${p.reading_time} min read</span>
        <div><a class="btn btn-light" href="/journal/${esc(p.slug)}" data-link>Read the story</a></div></div>`;
    } else feat.closest('section').remove();
    const items = l.results.filter((x) => !p || x.slug !== p.slug).slice(0, 5);
    latest.innerHTML = items.length ? `<div class="stories">${items.map((x, i) => storyCard(x, i === 0 ? 'lg' : 'md')).join('')}</div>` : statusBox('No stories yet.', 'Please check back soon.');
    observe();
  } catch {
    latest.innerHTML = errBox('data-retry-home');
    feat.closest('section')?.setAttribute('hidden', '');
  }
}

async function pickStart(id) {
  const s = STARTS.find((x) => x.id === id), box = $('#start-result');
  $$('[data-start]').forEach((b) => b.setAttribute('aria-pressed', String(b.dataset.start === id)));
  box.innerHTML = `<p class="label">Loading suggestions</p>`;
  try {
    const lists = await Promise.all(s.cats.map((c) => api(`/posts/?category=${c}&page_size=2`)));
    const seen = new Set(), picks = [];
    for (let i = 0; i < 2; i++) lists.forEach((l) => { const p = l.results[i]; if (p && !seen.has(p.slug)) { seen.add(p.slug); picks.push(p); } });
    box.innerHTML = `<h3 class="h-md">${esc(s.label)}</h3><p style="margin:10px 0 18px;color:var(--muted)">${esc(s.note)}</p>
      ${picks.slice(0, 3).map((p) => `<a class="mini" href="/journal/${esc(p.slug)}" data-link><img src="${img(p.hero_image)}" alt="" width="96" height="72" loading="lazy"><div><span class="label">${esc(p.category.name)}</span><h4>${esc(p.title)}</h4></div></a>`).join('')}
      <div class="row" style="margin-top:22px">${s.links.map((l, i) => `<a class="${i ? 'tlink' : 'btn btn-line btn-sm'}" href="${l[1]}" data-link>${esc(l[0])}</a>`).join('')}</div>`;
  } catch {
    box.innerHTML = `<p>We couldn't load suggestions right now.</p><div class="row" style="margin-top:16px">${s.links.map((l) => `<a class="tlink" href="${l[1]}" data-link>${esc(l[0])}</a>`).join('')}</div>`;
  }
}

/* ----- journal / categories ----- */
async function journal({ cat = '', params }) {
  const q = (params.get('q') || '').trim();
  const page = Math.max(1, parseInt(params.get('page') || '1', 10) || 1);
  const cats = await getCategories();
  const current = cats.find((c) => c.slug === cat);
  if (cat && !current) return notFound();
  const title = current ? current.name : 'The Journal';
  setMeta(q ? `Search: ${q}` : title + (page > 1 ? ` (page ${page})` : ''), current ? current.description : 'Stories on mind, body, nourishment, ritual, relationships and rest.');
  const base = cat ? `/category/${cat}` : '/journal';
  const qs = (o) => { const u = new URLSearchParams(); if (o.q) u.set('q', o.q); if (o.page > 1) u.set('page', o.page); const s = u.toString(); return s ? '?' + s : ''; };

  main.innerHTML = `<div class="wrap"><header class="page-head">
    <span class="label eyebrow">${current ? 'Category' : 'Stories'}</span>
    <h1 class="h-xl">${current ? esc(current.name) : 'The <em>Journal</em>'}</h1>
    <p class="lede">${current ? esc(current.tagline || current.description) : 'Slow reading on how to feel a little more like yourself.'}</p></header>
    <div class="tools">
      <nav class="chips" aria-label="Filter by category">
        <a class="chip" href="/journal${qs({ q })}" data-link ${!cat ? 'aria-current="true"' : ''}>All</a>
        ${cats.map((c) => `<a class="chip" href="/category/${esc(c.slug)}${qs({ q })}" data-link ${c.slug === cat ? 'aria-current="true"' : ''}>${esc(c.name)}</a>`).join('')}
      </nav>
      <form class="search" role="search" id="jsearch"><label class="sr" for="jq">Search stories</label>
        <input id="jq" name="q" type="search" placeholder="Search stories" value="${esc(q)}" autocomplete="off">
        ${q ? '<button class="clear" type="button" id="jclear" aria-label="Clear search">Clear</button>' : ''}<button type="submit">Search</button></form>
    </div>
    <div id="results" aria-live="polite" aria-busy="true">${skeleton()}</div></div>`;

  $('#jsearch').addEventListener('submit', (e) => { e.preventDefault(); go(base + qs({ q: $('#jq').value.trim() })); });
  $('#jclear')?.addEventListener('click', () => go(base));
  if (params.get('focus') === 'search') $('#jq').focus();

  const box = $('#results');
  try {
    const showFeat = page === 1 && !q && !cat;
    const url = `/posts/?page=${page}&page_size=${PAGE_SIZE}` + (cat ? `&category=${cat}` : '') + (q ? `&q=${encodeURIComponent(q)}` : '');
    const [data, f] = await Promise.all([api(url), showFeat ? api('/posts/?featured=true&page_size=1').catch(() => null) : null]);
    box.setAttribute('aria-busy', 'false');
    if (!data.count) {
      box.innerHTML = statusBox('No stories found.', q ? 'Try a different word or explore a category.' : 'There is nothing here yet. Please check back soon.', q ? `<a class="btn btn-line" href="${base}" data-link>Clear search</a>` : '');
      return;
    }
    const top = f?.results?.[0];
    const items = top ? data.results.filter((p) => p.slug !== top.slug) : data.results;
    const total = Math.ceil(data.count / PAGE_SIZE);
    const head = q ? `<p class="label" style="margin-bottom:26px">${data.count} ${data.count === 1 ? 'story' : 'stories'} for “${esc(q)}”</p>` : '';
    box.innerHTML = head + (top ? `<a class="top-feature rv" href="/journal/${esc(top.slug)}" data-link><div class="ph"><img src="${img(top.hero_image)}" alt="${esc(top.hero_image_alt)}" width="1600" height="1000"></div><div><span class="label">Featured · ${esc(top.category.name)}</span><h2 class="h-lg">${esc(top.title)}</h2><p class="ex">${esc(top.excerpt)}</p><p class="meta" style="margin-top:16px">${esc(top.author)}<span class="dot" aria-hidden="true">·</span>${top.reading_time} min read</p></div></a>` : '')
      + `<div class="stories">${items.map((p, i) => storyCard(p, i % 5 === 0 && page === 1 ? 'lg' : 'md')).join('')}</div>` + pager(page, total, base, q);
    observe();
  } catch (e) {
    box.setAttribute('aria-busy', 'false');
    box.innerHTML = e.status === 404 ? statusBox("That page doesn't exist.", 'You may have gone past the last page.', `<a class="btn btn-line" href="${base}" data-link>Back to the first page</a>`) : errBox('data-retry-journal');
  }
}

function pager(page, total, base, q) {
  if (total <= 1) return `<p class="pager"><span class="label">End of stories</span></p>`;
  const href = (n) => base + (() => { const u = new URLSearchParams(); if (q) u.set('q', q); if (n > 1) u.set('page', n); const s = u.toString(); return s ? '?' + s : ''; })();
  const nums = [];
  for (let n = 1; n <= total; n++) if (n === 1 || n === total || Math.abs(n - page) <= 1) nums.push(n); else if (nums[nums.length - 1] !== '…') nums.push('…');
  return `<nav class="pager" aria-label="Pagination"><a class="btn btn-line btn-sm" href="${href(page - 1)}" data-link ${page <= 1 ? 'aria-disabled="true" tabindex="-1"' : ''}>Previous</a>
    <div class="pages">${nums.map((n) => (n === '…' ? '<span>…</span>' : `<a href="${href(n)}" data-link ${n === page ? 'aria-current="page"' : ''} aria-label="Page ${n}">${n}</a>`)).join('')}</div>
    <a class="btn btn-line btn-sm" href="${href(page + 1)}" data-link ${page >= total ? 'aria-disabled="true" tabindex="-1"' : ''}>Next</a></nav>
    <p class="label" style="text-align:center;margin-top:14px">${page >= total ? 'You have reached the end' : `Page ${page} of ${total}`}</p>`;
}

/* ----- article ----- */
function renderBody(text) {
  return String(text).split(/\n{2,}/).map((b) => b.trim()).filter(Boolean)
    .map((b) => (b.startsWith('## ') ? `<h2>${esc(b.slice(3))}</h2>` : `<p>${esc(b).replace(/\n/g, '<br>')}</p>`)).join('');
}

async function article(slug) {
  main.innerHTML = `<div class="wrap">${skeleton()}</div>`;
  let p;
  try { p = await api(`/posts/${encodeURIComponent(slug)}/`); }
  catch (e) { return e.status === 404 ? notFound("We couldn't find that story.") : (main.innerHTML = `<div class="wrap">${errBox('data-retry-article')}</div>`); }
  setMeta(p.title, p.excerpt, p.hero_image);
  const ld = document.createElement('script'); ld.type = 'application/ld+json'; ld.id = 'ld';
  ld.textContent = JSON.stringify({ '@context': 'https://schema.org', '@type': 'Article', headline: p.title, description: p.excerpt, datePublished: p.published_at, author: { '@type': 'Person', name: p.author }, image: location.origin + img(p.hero_image), articleSection: p.category.name });
  document.head.appendChild(ld);

  main.innerHTML = `<article>
    <header class="art-head"><a class="label" href="/category/${esc(p.category.slug)}" data-link>${esc(p.category.name)}</a><h1>${esc(p.title)}</h1><p class="sub">${esc(p.excerpt)}</p>
      <p class="meta">By ${esc(p.author)}<span class="dot" aria-hidden="true">·</span><time datetime="${esc(p.published_at)}">${fmtDate(p.published_at)}</time><span class="dot" aria-hidden="true">·</span>${p.reading_time} min read</p></header>
    <figure class="art-hero" style="margin-bottom:54px"><img src="${img(p.hero_image)}" alt="${esc(p.hero_image_alt)}" width="1600" height="1000" fetchpriority="high"></figure>
    <div class="prose">${renderBody(p.content)}</div>
    <div class="art-actions"><button class="like" type="button" id="like" aria-pressed="${p.liked}"><span id="like-t">${p.liked ? 'Liked' : 'Like this story'}</span> · <span id="like-n">${p.like_count}</span></button>
      <a class="tlink" href="/journal" data-link>← Back to the journal</a><span id="like-msg" class="help" role="status"></span></div>
    <p class="note">This story is for general reflection and is not medical advice. If you are worried about your health, please speak with a qualified professional.</p>
    <section class="comments" aria-labelledby="cm-h"><h2 id="cm-h">Notes from readers</h2><div id="cm-form"></div><div id="cm-list">${skeleton()}</div></section>
  </article>
  <section class="related" aria-labelledby="rel-h"><div class="wrap"><h2 id="rel-h" class="h-lg" style="margin-bottom:34px">Related stories</h2><div id="related">${skeleton()}</div></div></section>`;

  const likeBtn = $('#like');
  likeBtn.addEventListener('click', async () => {
    if (!Auth.access) return go(`/login?next=${encodeURIComponent(location.pathname)}`);
    likeBtn.disabled = true;
    try {
      const liked = likeBtn.getAttribute('aria-pressed') === 'true';
      if (liked) { await api(`/posts/${slug}/like/`, { method: 'DELETE' }); } else { await api(`/posts/${slug}/like/`, { method: 'POST' }); }
      const fresh = await api(`/posts/${slug}/`);
      likeBtn.setAttribute('aria-pressed', String(fresh.liked)); $('#like-t').textContent = fresh.liked ? 'Liked' : 'Like this story'; $('#like-n').textContent = fresh.like_count;
    } catch { $('#like-msg').textContent = "That didn't go through. Please try again."; }
    likeBtn.disabled = false;
  });

  loadRelated(slug); loadComments(slug);
  observe();
}

async function loadRelated(slug) {
  const box = $('#related');
  try { const r = await api(`/posts/${slug}/related/`); box.innerHTML = `<div class="stories">${r.map((x) => storyCard(x, 'md')).join('')}</div>`; observe(); }
  catch { box.innerHTML = '<p class="help">Related stories are unavailable right now.</p>'; }
}

async function loadComments(slug) {
  const form = $('#cm-form'), list = $('#cm-list');
  form.innerHTML = Auth.access ? `<form class="form" id="cmf" novalidate style="margin-bottom:26px"><div class="field" data-field="content"><label for="cm-t">Leave a note</label><textarea id="cm-t" name="content" maxlength="1000" aria-describedby="cm-e" style="min-height:110px"></textarea><p class="err" id="cm-e" role="alert"></p></div><div><button class="btn btn-solid btn-sm" type="submit">Post note</button></div></form>`
    : `<p style="margin-bottom:22px;color:var(--muted)">Please <a href="/login?next=${encodeURIComponent(location.pathname)}" data-link style="color:var(--terra)">sign in</a> to leave a note. Notes are kept kind and short, and can be removed by their author or the editors.</p>`;
  $('#cmf')?.addEventListener('submit', async (e) => {
    e.preventDefault(); const f = e.target, btn = $('button', f), v = f.content.value.trim();
    if (v.length < 2) return setErr(f, 'content', 'Please write a little more.');
    clearErr(f); btn.disabled = true; btn.textContent = 'Posting…';
    try { await api(`/posts/${slug}/comments/`, { method: 'POST', body: { content: v } }); f.content.value = ''; await drawComments(slug); }
    catch (er) { setErr(f, 'content', er.status === 400 ? (er.data.content?.[0] || 'Please check your note.') : er.status === 401 ? 'Please sign in again.' : 'Something went wrong. Please try again.'); }
    btn.disabled = false; btn.textContent = 'Post note';
  });
  drawComments(slug);
}
async function drawComments(slug) {
  const list = $('#cm-list');
  try {
    const c = await api(`/posts/${slug}/comments/`);
    list.innerHTML = c.length ? c.map((x) => `<div class="cm"><span class="who">${esc(x.author)}</span><span class="when">${fmtDate(x.created_at)}</span><p>${esc(x.content)}</p>${x.can_delete ? `<button type="button" data-del="${x.id}" data-slug="${esc(slug)}">Remove</button>` : ''}</div>`).join('') : '<p class="help">No notes yet.</p>';
  } catch { list.innerHTML = '<p class="help">Notes could not be loaded.</p>'; }
}

/* ----- forms ----- */
function setErr(form, name, msg) { const f = $(`[data-field="${name}"]`, form); if (!f) return; f.dataset.invalid = 'true'; $('.err', f).textContent = msg; $('input,select,textarea', f).setAttribute('aria-invalid', 'true'); }
function clearErr(form) { $$('[data-field]', form).forEach((f) => { delete f.dataset.invalid; $('.err', f).textContent = ''; $('input,select,textarea', f).removeAttribute('aria-invalid'); }); }
const field = (id, label, input, extra = '') => `<div class="field" data-field="${id}"><label for="f-${id}">${label}</label>${input}<p class="err" id="e-${id}" role="alert"></p>${extra}</div>`;
const inp = (id, type, extra = '') => `<input id="f-${id}" name="${id}" type="${type}" aria-describedby="e-${id}" ${extra}>`;

function contact(params) {
  setMeta('Contact', 'Send a general enquiry to THE WITHIN. This form is not for urgent medical concerns.');
  const pre = params.get('topic') || '';
  main.innerHTML = `<div class="wrap"><header class="page-head"><span class="label eyebrow">Work with us</span><h1 class="h-xl">You can start with <em>a question.</em></h1></header>
  <div class="split sec" style="padding-top:20px"><div><p class="lede">Tell us a little about what you'd like to explore. There's no need to share anything private, and no pressure to know exactly what you need.</p><p class="help" style="margin-top:24px">This form is for general enquiries and is not intended for urgent medical concerns.</p></div>
  <div><div id="c-msg"></div><form class="form" id="cf" novalidate>
    ${field('name', 'Name', inp('name', 'text', 'autocomplete="name" required maxlength="100"'))}
    ${field('email', 'Email', inp('email', 'email', 'autocomplete="email" required'))}
    ${field('topic', 'What would you like to explore?', `<select id="f-topic" name="topic" aria-describedby="e-topic" required><option value="">Choose one</option>${['Therapy', 'Nutrition', 'Movement', 'Mindfulness', 'Wellness consultation', 'Not sure yet'].map((t) => `<option ${t === pre ? 'selected' : ''}>${t}</option>`).join('')}</select>`)}
    ${field('message', 'Message', '<textarea id="f-message" name="message" aria-describedby="e-message h-message" required maxlength="3000"></textarea>', '<p class="help" id="h-message">Please keep it general. Avoid sharing detailed medical information.</p>')}
    <div><button class="btn btn-solid" type="submit">Send enquiry</button></div></form></div></div></div>`;
  $('#cf').addEventListener('submit', async (e) => {
    e.preventDefault(); const f = e.target; clearErr(f); let bad = false;
    const d = Object.fromEntries(new FormData(f).entries()); d.name = d.name.trim(); d.message = d.message.trim();
    if (!d.name) { setErr(f, 'name', 'Please tell us your name.'); bad = true; }
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(d.email)) { setErr(f, 'email', 'Please enter a valid email address.'); bad = true; }
    if (!d.topic) { setErr(f, 'topic', 'Please choose a topic.'); bad = true; }
    if (d.message.length < 10) { setErr(f, 'message', 'Please write at least a sentence or two.'); bad = true; }
    if (bad) return $('[aria-invalid="true"]', f).focus();
    const btn = $('button', f); btn.disabled = true; btn.textContent = 'Sending…';
    try {
      await api('/contact/', { method: 'POST', body: d });
      $('#c-msg').innerHTML = '<p class="alert ok" role="status" tabindex="-1" style="margin-bottom:24px">Thank you. Your enquiry has been received and we will reply by email.</p>';
      f.reset(); $('#c-msg p').focus();
    } catch (er) {
      if (er.status === 400) Object.entries(er.data).forEach(([k, v]) => setErr(f, k, [].concat(v)[0]));
      else $('#c-msg').innerHTML = `<p class="alert" role="alert" style="margin-bottom:24px">${er.status === 429 ? 'Too many enquiries just now. Please try again later.' : 'We could not send that. Please try again.'}</p>`;
    }
    btn.disabled = false; btn.textContent = 'Send enquiry';
  });
}

function authPage(mode, params) {
  const reg = mode === 'register', next = params.get('next') || '/journal';
  setMeta(reg ? 'Create an account' : 'Sign in', 'Sign in to like stories and leave notes.');
  main.innerHTML = `<div class="wrap"><header class="page-head"><span class="label eyebrow">Readers</span><h1 class="h-lg">${reg ? 'Create an <em>account</em>' : 'Welcome <em>back</em>'}</h1><p class="lede">An account lets you like stories and leave notes. Nothing else.</p></header>
  <div style="padding-bottom:100px"><div id="a-msg"></div><form class="form" id="af" novalidate>
    ${field('username', 'Username', inp('username', 'text', 'autocomplete="username" required'))}
    ${reg ? field('email', 'Email', inp('email', 'email', 'autocomplete="email" required')) : ''}
    ${field('password', 'Password', inp('password', 'password', `autocomplete="${reg ? 'new-password' : 'current-password'}" required`), reg ? '<p class="help">At least 8 characters, not too common.</p>' : '')}
    <div class="row"><button class="btn btn-solid" type="submit">${reg ? 'Create account' : 'Sign in'}</button></div>
    <p class="help">${reg ? 'Already registered? <a href="/login" data-link style="color:var(--terra)">Sign in</a>' : 'New here? <a href="/register" data-link style="color:var(--terra)">Create an account</a>'}</p></form></div></div>`;
  $('#af').addEventListener('submit', async (e) => {
    e.preventDefault(); const f = e.target; clearErr(f); const d = Object.fromEntries(new FormData(f).entries()); let bad = false;
    if (!d.username?.trim()) { setErr(f, 'username', 'Please enter a username.'); bad = true; }
    if (reg && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(d.email || '')) { setErr(f, 'email', 'Please enter a valid email address.'); bad = true; }
    if (!d.password) { setErr(f, 'password', 'Please enter a password.'); bad = true; }
    if (bad) return;
    const btn = $('button', f); btn.disabled = true;
    try {
      if (reg) await api('/auth/register/', { method: 'POST', body: d });
      const t = await raw('/token/', { method: 'POST', body: { username: d.username, password: d.password } });
      Auth.set(t.access, t.refresh);
      const me = await raw('/auth/me/', { token: t.access }); Auth.set(t.access, t.refresh, me.name);
      renderAccount(); go(next.startsWith('/') ? next : '/journal');
    } catch (er) {
      if (er.status === 400) Object.entries(er.data).forEach(([k, v]) => setErr(f, k, [].concat(v)[0]));
      else $('#a-msg').innerHTML = `<p class="alert" role="alert" style="margin-bottom:24px">${er.status === 401 ? "That username and password don't match." : 'Something went wrong. Please try again.'}</p>`;
      btn.disabled = false;
    }
  });
}

/* ----- static pages ----- */
function about() {
  setMeta('About', 'The idea behind THE WITHIN: a journal and a small practice for people who want a more considered way to look after themselves.', 'img/about.svg');
  main.innerHTML = `<div class="wrap"><header class="page-head"><span class="label eyebrow">About</span><h1 class="h-xl">The idea behind <em>THE WITHIN</em></h1></header>
  <div class="split sec" style="padding-top:20px"><div class="pic rv" style="aspect-ratio:4/5;border-radius:999px 999px 0 0"><img src="/img/about.svg" alt="A calm interior with warm tones" width="1600" height="1000"></div>
    <div class="rv"><p class="big-p">We wanted a place that treats looking after yourself as ordinary, interesting and worth doing properly.</p><p style="margin-top:28px;color:var(--muted);max-width:56ch">THE WITHIN began as a simple observation: the best conversations about wellbeing happen slowly, and rarely on a screen full of rules. So we built a journal that reads like a magazine and a practice that feels like a conversation. Both are meant to leave you feeling a little more like yourself.</p></div></div>
  <section class="sec" style="padding-top:0"><span class="label eyebrow">Our approach</span><div class="about-cols">
    <article class="rv"><h3>Listen first</h3><p>We start with what you notice and what you want, not with a programme. Good care begins with attention.</p></article>
    <article class="rv"><h3>Keep it small</h3><p>Change tends to last when it is modest and repeatable. We favour a five-minute habit over a heroic plan.</p></article>
    <article class="rv"><h3>Stay honest</h3><p>We do not promise outcomes or claim to treat conditions. When something needs a doctor, we say so.</p></article></div></section>
  <section class="sec" style="padding-top:0"><span class="label eyebrow">Care in more than one form</span><h2 class="h-lg" style="max-width:16em">A conversation, a meal, a walk, a quiet <em>half hour.</em></h2>
    <p class="lede" style="margin-top:22px;max-width:60ch">Mind, body, food and ritual are not separate subjects. A difficult week affects how we eat; how we move changes how we think. The journal and the practice are organised around those connections, so you can start wherever feels easiest.</p></section>
  <section class="sec" style="padding-top:0"><div class="sec-head"><div><span class="label eyebrow">Our practitioners</span><h2 class="h-lg">The people <em>behind the practice.</em></h2></div><a class="tlink" href="/practitioners" data-link>Meet everyone</a></div>${peopleGrid(true)}</section></div>`;
  observe();
}
const peopleGrid = (brief) => `<div class="prac">${PEOPLE.map((p) => `<article class="rv"><div class="pic"><img src="/img/${p.img}.svg" alt="Placeholder portrait for ${esc(p.name)}, fictional ${esc(p.role.toLowerCase())}" width="1600" height="1000" loading="lazy"></div><h3>${esc(p.name)}</h3><span class="label">${esc(p.role)}</span>${brief ? `<p>${esc(p.approach)}</p>` : `<p>${esc(p.bio)}</p><dl><dt>Approach</dt><dd>${esc(p.approach)}</dd><dt>Area of focus</dt><dd>${esc(p.focus)}</dd></dl>`}</article>`).join('')}</div>`;

function practitioners() {
  setMeta('Practitioners', 'Meet the fictional practitioners of THE WITHIN.');
  main.innerHTML = `<div class="wrap"><header class="page-head"><span class="label eyebrow">Practitioners</span><h1 class="h-xl">Meet the <em>practice.</em></h1><p class="lede">Four fictional practitioners, one shared way of working: listen first, keep it small, stay honest.</p></header>${peopleGrid(false)}
  <p class="help" style="margin:40px 0 100px;max-width:62ch">These profiles are fictional and created for a portfolio concept. They do not represent real professionals or real qualifications.</p></div>`;
  observe();
}

function practice() {
  setMeta('The Practice', 'Individual therapy, nutrition, movement, mindfulness and wellness consultation at THE WITHIN, a fictional practice.', 'img/practice.svg');
  main.innerHTML = `<div class="wrap"><header class="page-head"><span class="label eyebrow">The practice</span><h1 class="h-xl">Five ways <em>to begin.</em></h1><p class="lede">Our sessions are for general wellbeing and reflection. They are not a substitute for medical care, and we do not promise specific outcomes.</p></header>
  ${SERVICES.map((s, i) => `<section class="svc-row rv" id="${s.id}" aria-labelledby="h-${s.id}"><div class="pic"><img src="/img/${s.img}.svg" alt="${esc(s.title)} at THE WITHIN" width="1600" height="1000" loading="lazy"></div><div><span class="label">0${i + 1}</span><h2 id="h-${s.id}" class="h-lg">${esc(s.title)}</h2><p>${esc(s.short)} ${esc(s.long)}</p><a class="btn btn-line" href="/contact?topic=${encodeURIComponent(s.topic)}" data-link>Ask about ${esc(s.name.toLowerCase())}</a></div></section>`).join('')}
  <p class="help" style="margin:30px 0 100px;max-width:62ch">THE WITHIN is not an emergency or crisis service. If you need urgent help, please contact your local emergency services.</p></div>`;
  observe();
}

function notFound(msg = "We couldn't find that page.") {
  setMeta('Page not found');
  main.innerHTML = `<div class="wrap">${statusBox('Nothing here.', msg, '<a class="btn btn-line" href="/journal" data-link>Back to the journal</a>')}</div>`;
}

/* ---------- router ---------- */
const routes = [
  [/^\/$/, () => home()],
  [/^\/journal\/?$/, (m, p) => journal({ params: p })],
  [/^\/journal\/([\w-]+)\/?$/, (m) => article(m[1])],
  [/^\/category\/([\w-]+)\/?$/, (m, p) => journal({ cat: m[1], params: p })],
  [/^\/about\/?$/, () => about()],
  [/^\/practice\/?$/, () => practice()],
  [/^\/practitioners\/?$/, () => practitioners()],
  [/^\/contact\/?$/, (m, p) => contact(p)],
  [/^\/login\/?$/, (m, p) => authPage('login', p)],
  [/^\/register\/?$/, (m, p) => authPage('register', p)],
];

let navToken = 0, popping = false;
async function route() {
  const t = ++navToken, url = new URL(location.href);
  closeMenu();
  const hit = routes.find((r) => r[0].test(url.pathname));
  try { hit ? await hit[1](url.pathname.match(hit[0]), url.searchParams) : notFound(); }
  catch (e) { console.error(e); main.innerHTML = `<div class="wrap">${errBox()}</div>`; }
  if (t !== navToken) return;
  $$('[aria-current="page"]').forEach((a) => a.removeAttribute('aria-current'));
  $$('.primary a, .secondary a, .mobile-menu nav>a, .mm-sub a').forEach((a) => { const u = new URL(a.href); if (u.pathname !== '/' && (url.pathname === u.pathname || url.pathname.startsWith(u.pathname + '/')) && !u.search.includes('focus')) a.setAttribute('aria-current', 'page'); });
  if (url.hash) document.getElementById(url.hash.slice(1))?.scrollIntoView(); else if (!popping) window.scrollTo(0, 0);
  main.focus({ preventScroll: true });
}
function go(path) { history.pushState({}, '', path); route(); }
window.addEventListener('popstate', () => { popping = true; route().then(() => { popping = false; }); });

/* ---------- global events ---------- */
document.addEventListener('click', (e) => {
  const so = e.target.closest('[data-signout]');
  if (so) { Auth.clear(); renderAccount(); return go('/'); }
  const del = e.target.closest('[data-del]');
  if (del) { del.disabled = true; api(`/comments/${del.dataset.del}/`, { method: 'DELETE' }).then(() => drawComments(del.dataset.slug)).catch(() => { del.disabled = false; del.textContent = 'Could not remove'; }); return; }
  if (e.target.closest('[data-retry-home]')) return route();
  if (e.target.closest('[data-retry],[data-retry-journal],[data-retry-article]')) return route();
  const a = e.target.closest('a[data-link]');
  if (a && !e.metaKey && !e.ctrlKey && !e.shiftKey && a.target !== '_blank') { e.preventDefault(); go(a.getAttribute('href')); }
});

const menuBtn = $('#menu-btn'), menu = $('#mobile-menu');
function closeMenu() { menu.hidden = true; menuBtn.setAttribute('aria-expanded', 'false'); document.body.classList.remove('menu-open'); }
menuBtn.addEventListener('click', () => {
  const open = menuBtn.getAttribute('aria-expanded') === 'true';
  if (open) closeMenu(); else { menu.hidden = false; menuBtn.setAttribute('aria-expanded', 'true'); document.body.classList.add('menu-open'); $('a', menu).focus(); }
});
document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) { closeMenu(); menuBtn.focus(); } });
matchMedia('(min-width: 901px)').addEventListener('change', closeMenu);
document.addEventListener('error', (e) => { const t = e.target; if (t.tagName === 'IMG' && !t.dataset.fb) { t.dataset.fb = '1'; t.src = '/img/hero.svg'; } }, true);

let io;
function observe() {
  io ||= new IntersectionObserver((es) => es.forEach((x) => { if (x.isIntersecting) { x.target.classList.add('in'); io.unobserve(x.target); } }), { rootMargin: '0px 0px -8% 0px' });
  $$('.rv:not(.in)').forEach((el) => io.observe(el));
}

renderAccount();
route();
