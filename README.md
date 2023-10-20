# Newsletter Generator

This Python script generates newsletters for the DCU Esports community. It uses a Jinja2 template to create customized newsletters with dynamic content.

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Web GUI](#web-gui)
- [Deploy on docker](#deploy-on-docker)
- [Directory Structure](#directory-structure)

## Getting Started

Follow the instructions below to get started with the DCU Esports Newsletter Generator.

### Prerequisites

- Python 3.x
- Jinja2 (Python template engine)
- Flask (for the web GUI)

You can install the requirements using pip:

```bash
pip install -r requirements.txt
```


### Usage

#### Manual Generation (auto_generate.py)

If you prefer the manual way of generating newsletters, follow these steps:

**Note:** Not all features are available in the manual generation method. Use the web GUI for the full experience.

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

#### Web GUI (app.py)

If you prefer a web GUI to generate newsletters, follow these steps:

1. Clone the repository
```bash
git clone git@github.com:aydenjahola/email-generator.git
```
2. Navigate to the project directory
```bash
cd email-generator
```
3. you can create your template in the `templates` directory. The template should include placeholders (using double curly braces) for dynamic content, which the script will replace.
4. Run the script
```bash
flask run --debug
```
5. Access the web GUI by opening a web browser and going to `http://localhost:5000`.
6. Fill out the form with the appropriate information and click `Generate Newsletter`.
7. The script will generate the newsletter, create an output directory based on the `week_number`, and save the newsletter in that directory.
8. You can find the generated newsletters in the `outputs` directory. Each newsletter is saved in a subdirectory named after the week number.

## Deploy on docker

to deploy on docker you can use the script `deploy.sh` to build and run the container

```bash
./deploy.sh
```


## Directory Structure

```bash
.
├── auto_generator.py
├── app.py
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
├── templates
│   └── newsletter_template.html
├── pages
│   ├── index.html
│   ├── success.html
│   ├── error.html
└── README.md
```

## TODO
- [x] ~~production server~~
- [ ] add more dynamic content
- [ ] add more newsletter templates
- [ ] add more newsletter examples
- [ ] add more documentation
- [ ] optimize the app more
- [ ] add more error handling
- [ ] add tests
- [ ] add copy button


## License

This project is licensed under the AGPLv3 License - see the [LICENSE](LICENSE) file for details.