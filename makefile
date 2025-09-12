create:
	@echo "Create VirtualEnv ..."
	python3 -m venv venv
	@echo "Done"

activate:
	@echo "Activate VirtualEnv ..."
	source venv/bin/activate
	@echo "Done"

upgrade:
	@echo "Upgrading..."
	pip install --upgrade pip
	@echo "Done"

install:
	@echo "Installing..."
	pip install -r requirements.txt
	@echo "Done"

run:
	python3 -m main