# FitAI — AI Clothing Recommendation & Virtual Try-On

FitAI is a research-focused fashion e-commerce prototype that combines personalized clothing recommendations with AI-powered virtual try-on.

The project supports a controlled comparison between:

- **FitAI experience** — preference-based product ranking and virtual try-on
- **Standard store experience** — a conventional product catalogue using the same products, prices, images, and stock

## Features

- Preference-based clothing recommendations
- Ranked top-three product matches
- AI virtual try-on powered by FASHN
- Shared catalogue of 16 clothing products
- Standard comparison storefront for user studies
- Responsive browser interface
- Flask backend with secure environment-variable configuration

## Technology

- Python and Flask
- JavaScript, HTML, and CSS
- FASHN Virtual Try-On API
- Render-ready deployment configuration

## Run locally

1. Create a Python virtual environment.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file:

   ```text
   FASHN_API_KEY=your_api_key
   ```

4. Start the application:

   ```bash
   python server.py
   ```

5. Open `http://127.0.0.1:5000/`.

The standard comparison store is available at `/normal.html`.

## Security

API credentials are never committed. Store the FASHN key in `.env` locally or as a secure environment variable on the hosting platform.

## Research context

FitAI was developed for an ICACT 2026 university research project examining how AI recommendations and virtual try-on influence usability, purchase confidence, and user satisfaction in fashion e-commerce.

## Author

**Sachith Raoshan**  
Portfolio research project — 2026
