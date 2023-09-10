
OUT=$(PWD)/dist
TOMLS:=$(shell find . -maxdepth 2 -name '*toml')
WHLS:=$(TOMLS:%.toml=%.whl)

wheels: $(WHLS)

clean:
	python -m pip uninstall -y $(TOMLS:./%/pyproject.toml=%)
	rm -f $(WHLS)
	rm -rf */*egg-info


#$(WHLS): %.whl: %.toml
#	cd $(shell dirname $<) && python -m build --outdir $(OUT) && cd .. && touch $@

$(WHLS): %.whl: %.toml
	cd $(shell dirname $<) && python -m pip install --no-deps -e . && cd .. && touch $@


$(OUT):
	mkdir $(OUT)

