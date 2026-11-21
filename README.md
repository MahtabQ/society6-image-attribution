# Society6 Image Attribution & Tagging Pipeline

An automated multimodal computer-vision and NLP pipeline built with **Python**, **LangChain**, and **Google Vertex AI (Gemini)** to classify artwork products across structured taxonomy attributes and generate high-value SEO keywords at scale.

---

## Key Capabilities

- **Multithreaded Image Ingestion & Normalization**: Concurrently downloads artwork images from product URLs and standardizes transparent/palette formats (`RGBA`, `LA`, `PNG`) onto a white-background `RGB` `.jpg` format.
- **Few-Shot Multimodal LLM Classification**: Uses Base64-encoded images, visual few-shot reference examples (*Ikat* vs. *Tie-Dyed*), and detailed taxonomy rubrics (with explicit inclusion/exclusion rules) to score attributes above a **70% confidence threshold**.
- **Parallel Processing & Token Tracking**: Processes batches concurrently via `ThreadPoolExecutor` while logging `input_tokens` and `output_tokens` per SKU for cost monitoring.
- **Brand, IP & Stopword Sanitization**: Validates categorical predictions against strict allowlists, removes product-type stopwords (e.g., *Throw Pillow*, *Wall Art*), and maps trademarked, brand, or celebrity terms to safe generic descriptors.
- **Automated Delivery & QA Exports**: Flattens ranked JSON predictions into wide numbered columns and outputs both delivery CSVs and Excel validation workbooks (with and without confidence scores).

---

## Project Architecture

```text
society6-image-attribution/
├── main.py                         # Pipeline orchestrator (CLI entry point & ThreadPoolExecutor)
├── examples/
│   ├── ikat.jpg                    # Few-shot visual example for Ikat pattern
│   └── tie_dyed.jpg                # Few-shot visual example for Tie-Dyed pattern
└── model/
    ├── image_enrichment.env        # Environment config (not committed; see Setup)
    ├── attribute_def.py            # Detailed definitions & rules for all 6 attribute groups
    ├── img_downloader.py           # Multithreaded image downloader & JPG converter
    ├── model_pipeline.py           # Vertex AI Gemini client, prompt builder & JSON parser
    ├── stopwords_removal.py        # Allowlist enforcement & keyword compliance filtering
    └── post_processing.py          # Wide-table reshaping & CSV/Excel report generation
