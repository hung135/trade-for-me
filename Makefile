clean:
	rm -rf build
	rm -rf dist
install:
	python setup.py install
test:
	python setup.py test
testrun: clean install
	trade_for_me 10 REP
runcode:
	python /workspaces/trade-for-me/src/trade_for_me/btc_climber.py 10 REP