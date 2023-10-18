from flask import Flask, render_template, request, redirect, url_for, flash
import os
from jinja2 import Environment, FileSystemLoader

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Define the template directory and file
template_dir = 'templates'
template_file = 'newsletter_template.html'

# Load the template
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template(template_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get dynamic data from the form
        dynamic_heading = request.form['dynamic_heading']
        week_number = request.form['week_number']
        intro = request.form['intro']

        # Get topics and tldr_data from the form
        topics = []
        tldrs = []

        for i in range(1, 4):
            topic_name = request.form[f'topic_name_{i}']
            topic_content = request.form[f'topic_content_{i}']
            tldr_content = request.form[f'tldr_content_{i}']

            topics.append({'topic_name': topic_name, 'topic_content': topic_content})
            tldrs.append({'tldr_content': tldr_content})

        # Create data dictionary
        data = {
            'dynamic_heading': dynamic_heading,
            'week_number': week_number,
            'intro': intro,
            'tldrs': tldrs,  # Pass the tldr data
            'topics': topics,
        }

        # Render the template with all the topic data
        output = template.render(data)

        # Define the directory for saving the newsletters
        output_directory = 'outputs'

        # Create a subdirectory based on the week_number
        week_directory = os.path.join(output_directory, f'week_{week_number}')

        # Create the subdirectory if it doesn't exist
        os.makedirs(week_directory, exist_ok=True)

        # Define the output file path
        output_file_path = os.path.join(week_directory, f'week_{week_number}_newsletter.html')

        # Save the generated newsletter with the updated file name
        with open(output_file_path, 'w', encoding='utf-8') as file:
            file.write(output)

        flash('Newsletter generated successfully!', 'success')
        return redirect(url_for('success'))

    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
