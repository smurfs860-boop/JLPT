# JLPT N3 Study Hub

A single-page website that helps you practice for JLPT N3 with:
- A quick-study planner you can check off as you go.
- Filterable vocabulary explorer covering common N3 terms.
- Grammar pattern notebook with concise meanings and examples.
- Mini practice cards that cycle between vocabulary and grammar prompts.

## Run locally

1. Install dependencies (consider a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
2. Start the backend API and static site:
   ```bash
   flask --app app run --debug
   ```
3. Visit [http://localhost:5000](http://localhost:5000) in your browser.

The site will use the API for vocabulary, grammar, planner tasks, and a randomized focus set. If the API is unavailable, it falls back to built-in data so the experience still works offline.
