import os
from jinja2 import Environment, FileSystemLoader

# Define the template directory and file
template_dir = 'templates'
template_file = 'newsletter_template.html'

# Load the template
env = Environment(loader=FileSystemLoader(template_dir))
template = env.get_template(template_file)

# Define dynamic data
dynamic_heading = "Let’s Get Spooky!"
week_number = "6"

# intro  after "hey nerds"
intro = """
    Welcome to the sixth edition of the DCU Esports Newsletter! We hope you're all doing well and are ready for some spooky fun. Halloween is just around the corner, and we're excited to share some of our plans with you. We've got a lot of exciting events coming up, so make sure to keep an eye out for announcements. We hope you enjoy this week's newsletter, and we'll see you in the next one!
        """

# Define a list to accumulate topics
topics = []
tldrs = []

# Define topic data
topic_data = [
    {
        'topic_name': 'Ireland Collegiate Esports Week 2',
        'topic_content': """
        The Ireland Collegiate Esports League continues to gain momentum, and we're thrilled to announce that Week 2 is just around the corner! Today, our teams will once again battle it out in various games, aiming for glory and the top of the leaderboard. To all our participating teams, we wish you the best of luck. Let's show them what DCU Esports is made of! 
        """,
    },
    {
        'topic_name': 'DCU B Team Triumphs on Valorant',
        'topic_content': """
        We're proud to share that our DCU B Team in Valorant recently achieved an impressive feat. They secured two victories and are now set to face off against some of the strongest teams in the league. It's fantastic to see our teams' hard work paying off, and we'll be cheering you on in your upcoming matches. 
        """,
    },
    {
        'topic_name': 'Valorant Bingo Event',
        'topic_content': """ Get ready for some fun and games because we'll be hosting a Valorant Bingo Event soon. Keep an eye out for announcements and make sure to join in the action. Prize, fun, and Valorant – what's not to love?""",
    },
    # Add more topics as needed
]

# Define tldr data
tldr_data = [
    {
        'tldr_content': 'This is the TL;DR for Topic 1.',
    },
    {
        'tldr_content': 'This is the TL;DR for Topic 2.',
    },
    {
        'tldr_content': 'This is the TL;DR for Topic 3.',
    },
]

# Accumulate topics in the 'topics' list
for topic in topic_data:
    topics.append({
        'topic_name': topic['topic_name'],
        'topic_content': topic['topic_content'],
    })
    
# Accumulate topics in the 'tldr' list
for tldr in tldr_data:
    tldrs.append({
        'tldr_content': tldr['tldr_content'],
    })


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

# Save or send the generated newsletter with the updated file name
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.write(output)

print("Newsletter generated successfully!")
