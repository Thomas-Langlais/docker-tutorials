# get the runtime image
FROM python:3.6-slim
# sets the working directoy
WORKDIR /app
# add the files to the wd, can be done many ways
COPY . /app
# installs the runtime dependencies, we can do 
# fancy devops settings here for the image with the capability
# to run commands
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# expose the port
EXPOSE 80
# Set the environment vars
# Can we do with dynamically from the cmd?
ENV ENV=TEST
# the command to run when the container launches
CMD ["python", "app.py"]