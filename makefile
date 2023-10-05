
OUT=$(PWD)/dist
TOMLS:=$(shell find . -maxdepth 2 -name '*toml')
WHLS:=$(TOMLS:%.toml=%.whl)
VENV_NAME=migrationplanning_venv
VENV_DIR=$(PWD)/$(VENV_NAME)

all: $(WHLS)

clean:
	python -m pip uninstall -y $(TOMLS:./%/pyproject.toml=%)
	rm -f $(WHLS)
	rm -rf */*egg-info


$(WHLS): %.whl: %.toml
	cd $(shell dirname $<) && python -m pip install --no-deps -e . && cd .. && touch $@

$(OUT):
	mkdir $(OUT)

$(VENV_NAME):
	WORKON_HOME=$(PWD) python3 -m venv $(VENV_DIR)
	@echo To enter venv, run: WORKON_HOME=$(PWD) source $(VENV_DIR)/bin/activate

rm_$(VENV_NAME):
	@echo To remove $(VENV_NAME), run: WORKON_HOME=$(PWD) rmvirtualenv migrationplanning_venv
