export PY_PATH = python

.PHONY: clean make_rst_from_markdown dist publish test_publish

clean:
	rm -fr ./build
	rm -fr ./dist

make_rst_from_markdown:
	pandoc -f markdown -t rst  README.md -o README.rst

dist: clean make_rst_from_markdown
	"${PY_PATH}" -m pip install 'twine>=1.5.0'
	"${PY_PATH}" setup.py sdist bdist_wheel

check_dist: dist
	twine check dist/*

publish: dist
	"${PY_PATH}" -m twine upload --repository pypi dist/*

test_publish: dist
	"${PY_PATH}" -m twine upload --repository testpypi dist/*