from flask import Flask, render_template, request, redirect, url_for, send_file, make_response
import os
from jinja2 import Environment, FileSystemLoader

# Initialize the Flask app
app = Flask(__name__)

# Define the template directory and file
template_dir = 'templates'

# Function to get a list of available templates


def get_available_templates():
    template_files = []
    for root, _, files in os.walk(template_dir):
        for file in files:
            template_path = os.path.join(root, file)
            if not template_path.startswith(os.path.join(template_dir, "pages")):
                template_files.append(file)
    return template_files


@app.route('/', methods=['GET', 'POST'])
def index():

    # Get the list of available templates
    template_files = get_available_templates()

    if request.method == 'POST':

        # Get selected template from the dropdown menu
        selected_template = request.form['selected_template']

        # Load the selected template
        template_file = os.path.join(template_dir, selected_template)
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template(selected_template)

        # Get dynamic data from the form
        dynamic_heading = request.form['dynamic_heading']
        week_number = request.form['week_number']
        intro = request.form['intro']

        # Initialize empty lists for topics and tldrs
        topics = []
        tldrs = []

        # Loop through form fields to collect topics and tldrs
        for field_name in request.form:
            if field_name.startswith('topic_name_'):
                topic_index = field_name.split('_')[-1]
                topic_name = request.form[field_name]
                topic_content = request.form.get(
                    f'topic_content_{topic_index}')
                tldr_content = request.form.get(f'tldr_content_{topic_index}')

                if topic_name:
                    topics.append({
                        'topic_name': topic_name,
                        'topic_content': topic_content,
                    })

                if tldr_content:
                    tldrs.append({
                        'tldr_content': tldr_content,
                    })

        # Create data dictionary
        data = {
            'dynamic_heading': dynamic_heading,
            'week_number': week_number,
            'intro': intro,
            'topics': topics,
            'tldrs': tldrs,
        }

        # Define the directory for saving the newsletters
        output_directory = 'outputs'

        # Create a subdirectory based on the week_number
        week_directory = os.path.join(output_directory, f'week_{week_number}')

        # Create the subdirectory if it doesn't exist
        os.makedirs(week_directory, exist_ok=True)

        # Define the output file path
        output_file_path = os.path.join(
            week_directory, f'week_{week_number}_newsletter.html')

        # Render the template with all the topic data
        output = template.render(data)

        # Save the generated newsletter with the updated file name
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(output)

        return redirect(url_for('success', week_number=week_number))

    return render_template('pages/index.html', template_files=template_files)


@app.route('/success/<week_number>', methods=['GET'])
def success(week_number):
    return render_template('pages/success.html', week_number=week_number)


@app.route('/download/<week_number>', methods=['GET'])
def download(week_number):
    try:
        # Define the file path for the generated newsletter
        newsletter_file_path = os.path.join(
            'outputs', f'week_{week_number}', f'week_{week_number}_newsletter.html')
        return send_file(newsletter_file_path, as_attachment=True)
    except FileNotFoundError:
        return render_template('pages/error.html')


@app.route('/view_generated_newsletter/<week_number>', methods=['GET'])
def view_generated_newsletter(week_number):
    # Define the file path for the generated newsletter
    newsletter_file_path = os.path.join(
        'outputs', f'week_{week_number}', f'week_{week_number}_newsletter.html')

    try:
        # Open and read the newsletter content
        with open(newsletter_file_path, 'r', encoding='utf-8') as file:
            newsletter_content = file.read()

        # Create a response to display the content
        response = make_response(newsletter_content)
        response.headers["Content-Type"] = "text/html"
        return response
    except FileNotFoundError:
        return render_template('pages/error.html')


if __name__ == '__main__':
    app.run(debug=True)
