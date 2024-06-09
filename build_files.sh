echo "BUILD START"
# Install dependencies from requirements.txt
python3.9 -m pip install -r requirements.txt

# Ensure Django is installed and collect static files
python3.9 -m pip install django  # Install Django if not already installed
python3.9 manage.py collectstatic --noinput --clear

echo "BUILD END"
