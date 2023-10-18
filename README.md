# DCU Esports Newsletter Generator

This Python script generates newsletters for the DCU Esports community. It uses a Jinja2 template to create customized newsletters with dynamic content.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Directory Structure](#directory-structure)

## Getting Started

Follow the instructions below to get started with the DCU Esports Newsletter Generator.

### Prerequisites

- Python 3.x
- Jinja2 (Python template engine)
  
You can install Jinja2 using pip:
```bash
pip install Jinja2
```

### Usage

1. Clone the repository
```bash
git clone git@github.com:aydenjahola/email-generator.git
```
2. Navigate to the project directory
```bash
cd email-generator
```
3. Prepare your newsletter content by modifying the script. You can update the `topic_data`, `tldr_data`, and other dynamic content as needed.
4. Create your newsletter template in HTML format. The template should include placeholders (using double curly braces) for dynamic content, which the script will replace.
5. Save the newsletter template in the `templates` directory.
6. Update the script with the appropriate file paths and dynamic content.
7. Run the script
```bash
python3 auto_generator.py
```
8. The script will generate the newsletter, create an output directory based on the `week_number`, and save the newsletter in that directory.
9. You can find the generated newsletters in the `outputs` directory. Each newsletter is saved in a subdirectory named after the week number.

## Directory Structure

```bash
.
├── auto_generator.py
├── outputs
│   ├── week_1
│   │   └── week_1_newsletter.html
│   ├── week_2
│   │   └── week_2_newsletter.html
│   ├── week_3
│   │   └── week_3_newsletter.html
│   ├── week_4
│   │   └── week_4_newsletter.html
│   ├── week_5
│   │   └── week_5_newsletter.html
|-- templates
│   └── newsletter_template.html
└── README.md
```