clean:
	rm -rf build
	rm -rf dist
install:
	python setup.py install
test:
	python setup.py test
testrun:
	trade_for_me 10 REP