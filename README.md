# JLPT N3 Study Hub

A single-page website that helps you practice for JLPT N3 with:
- A quick-study planner you can check off as you go.
- Filterable vocabulary explorer covering common N3 terms.
- Grammar pattern notebook with concise meanings and examples.
- Mini practice cards that cycle between vocabulary and grammar prompts.

## Run locally

No external dependencies are required (Python 3.11+). From the repo root, start the server and open the site:

```bash
python app.py
```

Visit [http://localhost:5000](http://localhost:5000) in your browser.

The app serves both the static site and simple JSON endpoints for vocabulary, grammar, planner tasks, and a focus set. If requests fail, the frontend falls back to its built-in data so the experience keeps working offline.
