run:
	@ echo 'run assessment ..'
	@ python assessment.py
test:
	@ echo 'start tests ..'
	@ coverage run -m --source=. pytest ./tests -v
	@ coverage report -m
	@ coverage html -d coverage_html
	@ open -a "Google Chrome" ./coverage_html/index.html
