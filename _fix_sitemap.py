# Post-render: list the home page in the sitemap as "/" to match its canonical URL.
import os
out = os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "docs")
p = os.path.join(out, "sitemap.xml")
if os.path.exists(p):
    s = open(p).read()
    s = s.replace("<loc>https://faboagye.github.io/index.html</loc>", "<loc>https://faboagye.github.io/</loc>")
    open(p, "w").write(s)
