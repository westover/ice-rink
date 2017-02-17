help:
	# Hack for the makefile to provide some info
	cat Makefile | grep "^\w" | awk '{print $$1}' | sed "s/://g"

# Build a virtual environment from specifications in the repo's env folder
# Install packages from requirements.txt using pip
build_env:
	virtualenv env
	env/bin/pip install -r requirements.txt

# Remove all .pyc and __pycache__ files from the repo
clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf __pycache__