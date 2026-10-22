# Cloudflare Pages migration plan

Prepared 22 October 2026, after deploying and verifying the approved website changes. **Planning only: no Cloudflare Pages project, DNS change, GitHub Pages shutdown, or hosting migration was performed.**

## Current, verified deployment

The website is still hosted by **GitHub Pages**, with **Cloudflare DNS and reverse proxy** in front of it.

- Repository: `https://github.com/velhud/romanempire-fr`.
- GitHub Pages publishing source: branch `main`, repository root `/`, legacy/branch publishing.
- Custom domain: `romanempire.fr`; the repository `CNAME` contains that domain.
- GitHub-generated workflow: `pages build and deployment`; it builds with Jekyll and deploys to GitHub Pages. There is no repository-managed deployment workflow to move wholesale.
- Approved website release: `569c87798ef355538eae6ef54a02e20ba3eda078`, successfully built and deployed on 22 October 2026. [Successful release workflow](https://github.com/velhud/romanempire-fr/actions/runs/39827664955).
- Follow-up logo-spacing correction: `a4bc96b476ae765f70a48e381e3c9c705f814df0`. It adds whitespace inside the white logo panel while preserving the horizontal frame dimensions. Recheck the latest `main` and deployment record when executing this plan.
- Public HTML shows the optimized portrait, inAi.world branding, and horizontal logo frame. Sixteen checked public assets match the release files. EN/FR/RU, mobile logo proportions, email decoding, keyboard activation, and repeated reduced-motion carousel movement were verified on the public domain.
- Public nameservers are `anirban.ns.cloudflare.com` and `fish.ns.cloudflare.com`. HTTP responses include both Cloudflare and GitHub-origin headers. The Cloudflare addresses returned by public DNS are edge addresses; they are not a rollback record of the configured origin.
- GitHub's Pages setting currently reports `https_enforced: false`; the observed public HTTPS endpoint works through Cloudflare. Do not change that setting as an unrelated part of this plan.

Today, a normal approved push to `origin/main` triggers the existing GitHub Pages deployment. Check the workflow outcome and the public website before calling a release complete.

## Intended end state

Cloudflare handles DNS, HTTPS delivery, and static hosting through **Cloudflare Pages**. GitHub remains the source repository, connected to Pages for automatic deployment of `main`. GitHub Pages publishing is disabled after the replacement is proven.

Keep the current appearance, frames, layout, wording, locales, optimized images, and inAi World logo. This migration does not reopen the rejected redesign. The inspected site is static HTML/CSS/JavaScript; it needs no framework rewrite, application server, database, or application secrets.

## 1. Inspect the existing Cloudflare account before changing anything

When Roman authorizes migration, use the existing account that owns the `romanempire.fr` zone. Check for an existing Pages project before creating a duplicate. Verify access to that zone and to the repository's Cloudflare GitHub integration.

Save a private rollback snapshot of the actual apex and `www` DNS records and relevant redirect/cache/Worker-route settings. Record their IDs, targets, proxy state and TTL. Preserve unrelated DNS records, including mail and verification records. Do not put account tokens or private zone exports into this public repository.

The authenticated Cloudflare account, actual proxied origin record values, existing Pages projects, and current zone redirect rules were not inspected during preparation. Resolve those facts at this step; nameservers and `server: cloudflare` alone do not identify a Pages deployment.

## 2. Prepare a parallel Pages deployment

Use the Pages **Git integration** with the existing repository. Cloudflare can deploy automatically on Git pushes; authorize the integration for the intended repository while retaining any existing legitimate access for other projects. [GitHub integration documentation](https://developers.cloudflare.com/pages/configuration/git-integration/github-integration/).

Suggested project name: `romanempire-fr`, subject to account inventory and availability. The eventual `pages.dev` hostname must come from the created project's actual response.

| Setting | Value for this repository |
|---|---|
| Product | Cloudflare Pages |
| Repository | `velhud/romanempire-fr` |
| Production branch | `main` |
| Framework preset | None |
| Root directory | Repository root |
| Build command | `exit 0` |
| Build output directory | `.` — the directory containing `index.html` |
| Application environment variables | None required by the inspected site |

The static HTML guide supports deployment without a site generator and documents the no-op build command. Do not run the old `build_i18n_js.py` during deployment: the current served runtime reads inline translations from `index.html`. [Static HTML deployment documentation](https://developers.cloudflare.com/pages/framework-guides/deploy-anything/).

The release contains 81 tracked files; the largest is the preserved `picture.png`, 15,892,019 bytes. These are below the documented Pages limits of 20,000 files on Free and 25 MiB per asset. Recheck the actual publish tree at migration time; no image deletion is required for these limits. [Pages limits](https://developers.cloudflare.com/pages/platform/limits/).

Deploy to the project's `pages.dev` address first, keeping production DNS on GitHub Pages. Record the Pages deployment ID and Git commit. Compare the rendered site and assets there before attaching the production domain.

## 3. Address two hosting differences before cutover

**Canonical hostname redirect.** The current `_redirects` file contains:

```text
https://www.romanempire.fr/*  https://romanempire.fr/:splat  301!
```

Do not carry this forward as a working Pages redirect. Pages expects a path-based source and numeric status; its redirect documentation does not support general domain-level redirects through this file. Replace this legacy entry with a comment or omit it from the Pages output once the hostname redirect is handled in Cloudflare. Do not broaden a redirect to unrelated hosts. [Pages redirect syntax](https://developers.cloudflare.com/pages/configuration/redirects/).

Reuse an existing verified Cloudflare `www` redirect if suitable. Otherwise follow Cloudflare's documented Bulk Redirect pattern: `www.romanempire.fr` to `https://romanempire.fr`, HTTP 301, preserving query strings and path suffixes with subpath matching. Ensure the exact `www` name has a proxied DNS record; the documented redirect-only pattern uses `A 192.0.2.1`. Save and replace the current record deliberately, and verify that `www` no longer depends on GitHub. [Cloudflare's www-to-apex procedure](https://developers.cloudflare.com/pages/how-to/www-redirect/).

**Unknown paths.** There is no top-level `404.html`. GitHub Pages currently returns a real 404 for unknown paths; Pages defaults to an SPA fallback without this file. Add a small top-level `404.html` as a migration compatibility change and verify HTTP 404. Preserve browser-side hash routes such as `/#cv` and `/#inai`. Start with Pages' normal caching defaults; avoid adding a cache-everything rule or immutable caching for stable filenames such as `assets/js/i18n.js`. [Serving and caching behavior](https://developers.cloudflare.com/pages/configuration/serving-pages/).

Publish these compatibility changes and verify the Pages deployment before the DNS switch. Keep the GitHub-hosted site available as the rollback origin during this phase.

## 4. Move the production domain

After the parallel site passes, use the Pages project's **Custom domains** flow to associate `romanempire.fr`. Inspect and confirm the resulting apex DNS change in the existing Cloudflare zone. Add the custom domain association before relying on a CNAME to the Pages hostname; a standalone CNAME without that association can fail. Nameservers already point to Cloudflare, so a registrar/nameserver migration is not part of this operation. [Custom domain setup](https://developers.cloudflare.com/pages/configuration/custom-domains/).

Confirm certificate activation and public HTTPS, then apply or validate the narrow `www` redirect. Preserve `https://romanempire.fr/` as the canonical URL, sitemap location, and public address. Do not rename the site domain as part of moving its host.

## 5. Verify the production cutover

Completion requires the Pages dashboard/deployment record to identify the production commit and active domain, as well as public behavior. Cloudflare response headers alone do not prove which origin serves the content.

- Apex HTTPS returns the correct page. HTTP and `www` reach the canonical HTTPS apex without a loop; paths and query strings survive the hostname redirect.
- Portrait, current logo, historical logos and i18n script are served successfully and match the intended deployment files. No stale pre-optimization page remains.
- EN/FR/RU selection and persistence, profile/project dialogs, direct hash reload, Escape/Back behavior, keyboard activation, touch swipe, and both carousel loop boundaries work, including reduced motion.
- Desktop and mobile preserve the approved composition; the horizontal logo's badge clears the artwork. No horizontal overflow or unexpected browser errors appear.
- Both visible contact links remain `mailto:ave@romanempire.fr`. Test the real browser after any Cloudflare email obfuscation; do not send mail merely to test the hosting move.
- Robots, sitemap, social-image URLs and icons serve; unknown paths return 404.

During the October release check, Python urllib received a 403 while curl and Chrome succeeded. If that difference persists after cutover, inspect the relevant Cloudflare rule/event before treating it as missing content. Do not weaken zone protection automatically.

## 6. Retire GitHub Pages after a stable cutover

Keep the old publishing source available until production checks pass and the migration operator is satisfied that rollback is no longer immediately needed. Then set the repository's GitHub Pages publishing branch to **None**, retaining the repository and its history. Merely unpublishing a deployment is temporary and can be undone by another successful build. [Disable publishing by changing the source](https://docs.github.com/en/pages/getting-started-with-github-pages/deleting-a-github-pages-site).

Remove the obsolete repository `CNAME` in a documented retirement commit after disabling GitHub Pages, preserving its previous value in Git history. Confirm that future approved pushes deploy through Cloudflare Pages only and that apex/`www` DNS has no remaining GitHub-hosting dependency. Update `README.txt` with the actual Pages project, production URL and release verification commands.

## Rollback

Before GitHub Pages retirement, restore the saved apex/`www` DNS targets and redirect configuration if the new origin or certificate fails. The previously verified GitHub Pages site must still be available for this route. If retirement has already happened, restore its publishing source and `CNAME`, wait for a successful build, and then restore DNS; do not route traffic to an unpublished origin.

For a later bad Cloudflare release, use a previously successful **production** Pages deployment as the rollback target. Preview deployments are not production rollback targets. [Pages rollback procedure](https://developers.cloudflare.com/pages/configuration/rollbacks/).

The migration is complete when production hosting and subsequent deployments run through Cloudflare Pages, the approved behavior remains intact, and GitHub Pages publishing is disabled. Until then, describe the migration as prepared or in progress.
