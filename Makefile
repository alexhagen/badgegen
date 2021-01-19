TESTS := $(wildcard test/test_*.py)
PYFILES := $(wildcard badgegen/*.py)

doc: FORCE
	sphinx-build -M html doc/source doc/build

test: $(PYFILES) $(TESTS)
	pytest --ignore=sandbox/ --cov=./ --cov-report=html --cov-config=.coveragerc | tee doc/source/_static/doc_test.txt

todo: $(PYFILES)
	leasot $(PYFILES) --filetype=.py | tee -a todos.md

lint: FORCE
	pylint $(PYFILES) | tee todos.md

FORCE:
