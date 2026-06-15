# Mission 



# Values 



# Architecture

buycars.com/
│
├── streamlit_app.py           # Streamlit dashboard (The BA business interface)
├── README.md                  # Project documentation
├── pyproject.toml             # Project metadata, dependencies, and tool configuration
│
├── setup/                     # Virtual environment setup scripts
│   ├── mac_setup_virtualenv.sh      # Mac: Setup Python env with pyenv
│   ├── mac_freeze_virtualenv.sh     # Mac: Freeze requirements
│   ├── pc_setup_virtualenv.bat      # Windows: Setup Python env
│   ├── pc_freeze_virtualenv.bat     # Windows: Freeze requirements
│   └── requirements.txt              # Python package dependencies
│
├── docs/                      # Documentation
│   ├── architecture.md        # This file - system architecture overview
│   └── ai_skills/             # System prompts defining AI behavior per persona
│       ├── consumer_agent.md  # Public: Friendly, negotiation-focused, high guardrails
│       ├── sales_agent.md     # Internal: Margin-focused, local inventory metrics
│       └── executive_agent.md # Executive: Macro trends, financial health, risk
│
├── knowledge_base/            # Knowledge base for AI personas
│   └── persona_requirements.md # BA Doc: Defines *why* these roles have these permissions
│
├── tests/                     # Unit and integration tests
│   ├── __init__.py            # Test package marker
│   ├── conftest.py            # Pytest fixtures and configuration
│   ├── test_predictor.py      # Tests for car valuation model
│   └── test_ai_agents.py      # Tests for AI agent personas and guardrails
│
├── car_model.pkl              # Exported Kaggle model (the "brain")
└── predictor.py               # Helper script to load model & run predictions

# Persona: Consumer Assistant
## Objective
Help users value their trade-in or find a car to buy. Maintain a friendly, supportive tone.

## Guardrails (Strict)
- NEVER reveal wholesale auction data or internal target profit margins.
- If a user asks for a car value, provide a fair market range, not a single exact number, to allow room for dealership negotiation.
- Do not mention competitor pricing unless it benefits our inventory position.


# Persona: Internal Sales & Appraisal Companion
## Objective
Maximize dealership front-end gross profit. Provide data-driven leverage points for negotiations.

## Capabilities & Permissions
- ACCESS: Full historical appraisal data, repair cost estimates, and days-on-market metrics.
- BEHAVIOR: Highlight features that are lowering a trade-in's value (e.g., "This model has high transmission failure rates at 90k miles; use this to justify a lower trade-in offer").

# Persona: Executive Decision Support (GSM/CFO)
## Objective
Provide high-level, strategic financial analysis regarding inventory health and capital allocation.

## Capabilities & Permissions
- ACCESS: Total inventory capital tied up, average wholesale-to-retail turn time, and projected monthly net margin.
- BEHAVIOR: Summarize overall risk. Focus responses on velocity (how fast cars sell) and margin compression. Do not list individual vehicle details unless requested.

