# random generator
Random generator with predefined set of probabilities and set of numbers.   
Numbers and probabilities are hardcoded.You can change them with equal by length lists.  

## Usage  
Generator can be used as module or just as file or class (copy) in your code.  
Generator was tested with python 3.10.9 (should work with 3.6 and newest) .  
All example commands was presented consider using bash (unix-like OS or WSL)
### Clone repository
```bash
# https
git clone https://github.com/antoan-georgiev/random_generator_with_predefined_probabilities.git
```  

### 1 Test it directly  
### Create virtual environment
It's recommended to create virtual environment for project (virtualenv and pyenv example)
```bash
cd random_generator_with_predefined_probabilities # <project-root-dir>
virtualenv --python==3.10.9 ./.vienv
# or 
virtualenv --python==/home/<user>/.pyenv/versions/3.10.9 ./.vienv
# then
source ./vienv/bin/activate
```  
### Run generator manually:
add this two lines in the end of random_num.py file:
```python
generator = RandomGen()
print(generator.next_num())
```  
and run commnd:  
```bash
python ./generator/random_num.py
```  
### Run tests
```bash
python ./generator/test_next_random_num.py
```  

### 2 Test it with Docker
You should have Docker installed (use 'sudo' if needed)
### Build image
```bash
docker build -t generator .
```  
Note: this image is not mentioned for production!  

### Run container
```bash
docker run --rm -it --name test-generator generator
```  
You shall see result from test:
```bash
$ docker run --rm -it --name test-generator generator
1
..
----------------------------------------------------------------------
Ran 2 tests in 0.024s

OK
```  
Container will be closed and deleted automatically.  

To change behavior change directives 'ENTRYPOINT' and 'CMD' with 'RUN echo ./*'.  
Rebuild and run image with command:  
```
docker run --rm -it --name test-generator generator /bin/sh
```  
now container shell will stay open adn you can run test as many times you wish:  
```bash
python test_next_random_num.py
```  
Type 'exit' to close and delete container. 

### Clean up
To clean up after testing run  
```bash
$ docker image rm generator
```  
