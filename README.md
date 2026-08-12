# FitAI — AI Clothing Recommendation & Virtual Try-On

FitAI is a research-focused fashion e-commerce prototype combining personalized clothing recommendations with AI-powered virtual try-on.

## Project overview

This project supports a controlled comparison between two shopping experiences:

- **FitAI** — preference-based product ranking and AI virtual try-on
- **Standard store** — a conventional catalogue using the same products, prices, images, and stock

## Key features

- Preference-based clothing recommendations
- Ranked top-three product matches
- AI virtual try-on powered by FASHN
- Shared catalogue of 16 clothing products
- Standard comparison storefront for user studies
- Responsive browser interface
- Secure Flask backend configuration
- Render-ready deployment

## Technology

- Python and Flask
- JavaScript, HTML, and CSS
- FASHN Virtual Try-On API
- Gunicorn for production serving
- Render for cloud deployment

## Local setup

1. Create and activate a Python virtual environment.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add your FASHN API key:

   ```text
   FASHN_API_KEY=your_api_key
   ```

4. Start the application:

   ```bash
   python server.py
   ```

5. Open `http://127.0.0.1:5000/`.

The standard comparison store is available at `/normal.html`.

## Deployment

The included `render.yaml` describes the web service. Add `FASHN_API_KEY` as a secret environment variable in Render before deploying.

## Security

The real `.env` file is excluded from version control. Never commit API keys or other credentials.

## Research context

FitAI was developed for an ICACT 2026 university research project examining how AI recommendations and virtual try-on influence usability, purchase confidence, and user satisfaction in fashion e-commerce.

## Author

**Sachith Raoshan**  
Portfolio research project — 2026
