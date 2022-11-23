#base docker image
FROM python:3



#creating working directory in virtual environment
WORKDIR /usr/src/app

#copying files from local machine to virtual machine
COPY TreeProblemSolution.py .
COPY test.py .
COPY restaurant_log_app.py .
COPY log_of_top_list.csv .
COPY log_of_top_3_list.csv .
COPY log_list_1.csv .
COPY empty_log_list.csv .
COPY create_csv.py .
COPY __init__.py .
#where i only need pands library so commented requirements.txt file
#COPY requirements.txt .

#installing prerequesites
RUN pip install --upgrade pip
RUN pip install --no-cache-dir pandas

#run test.py file
ENTRYPOINT ["python3"]
CMD ["test.py","restaurant_log_app.py"] 