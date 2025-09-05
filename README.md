# noteslens-repo
Classifies and summarizes content
<!--First Push by Manoj --> 
notelens/
├─ backend/        # API service (FastAPI/Flask) and core logic
│  ├─ retrieval/   # Search modules (keyword, vector, hybrid)
│  ├─ prompts/     # System/answer prompt templates & guardrails
│  └─ utils/       # Helpers (logging, config, error handling)
├─ frontend/       # User interface (Next.js/React app)
│  ├─ components/  # Reusable UI components (SearchBox, ResultsList, etc.)
│  ├─ pages/       # App pages (search, standard details)
│  └─ styles/      # Styling (CSS/Tailwind configs)
├─ data/           # Standards data and schema
│  ├─ seed/        # Small sample datasets for local/dev testing
│  └─ schema/      # Database schemas and migrations
├─ ingestion/      # Scripts to parse, normalize, and load standards
├─ tests/          # Unit and integration tests
├─ scripts/        # Dev tools (bootstrap DB, embeddings, etc.)
└─ docs/           # Project documentation and guides
