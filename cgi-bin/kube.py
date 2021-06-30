#!/usr/bin/python3 

print("content-type: text/html")
print()

import cgi 
import subprocess

import json
import openai

from gpt import GPT
from gpt import Example

openai.api_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

gpt = GPT(engine="davinci",
          temperature=0.5,
          max_tokens=100)

gpt.add_example(Example('Launch a web deployment with vimal13/apache-webserver-php image',
                        'kubectl create deployment web --image=vimal13/apache-webserver-php'))
gpt.add_example(Example('run a deployment httpd with httpd image',
                        'kubectl create deployment httpd --image=httpd'))
gpt.add_example(Example('Show me the pods',
                        'kubectl get pods'))
gpt.add_example(Example('Show me the deployments',
                        'kubectl get deployment'))
gpt.add_example(Example('Show me the service',
                        'kubectl get svc'))
gpt.add_example(Example('Launch a test deployment with httpd image',
                        'kubectl create deployment web --image=httpd'))
gpt.add_example(Example('Launch a test pod with vimal13/apache-webserver-php image',
                        'kubectl run test --image=vimal13/apache-webserver-php'))
gpt.add_example(Example('Launch a webserver pod with httpd image',
                        'kubectl run pod webserver --image=httpd'))
gpt.add_example(Example('Launch a pod with webpod as name and vimal13/apache-webserver-php as image',
                        'kubectl run webpod --image=vimal13/apache-webserver-php'))
gpt.add_example(Example('Delete deployment with name webserver',
                        'kubectl delete deployment webserver'))
gpt.add_example(Example('Delete a pod with name teting',
                        'kubectl delete pod testing'))
gpt.add_example(Example('Expose the deployment webserver as NodePort type and on port 80',
                        'kubectl expose deployment webserver --port=80 --type=NodePort'))
gpt.add_example(Example('Expose the deployment webapp as ClusterIP type and on port 80',
                        'kubectl expose deployment webapp --port=80 --type=ClusterIP'))
gpt.add_example(Example('Expose the deployment webtest as External LoadBalancer type and on port 80',
                        'kubectl expose deployment webtest --port=80 --type=LoadBalancer'))
gpt.add_example(Example('Create 5 replicas of test deployment',
                        'kubectl scale deployment test --replicas=5'))
gpt.add_example(Example('Create 3 replicas of webapp deployment',
                        'kubectl scale deployment webapp --replicas=3'))
gpt.add_example(Example('Delete all resources of Kubernetes',
                        'kubectl delete all --all'))

f = cgi.FieldStorage()
prompt = f.getvalue('x')

output = gpt.submit_request(prompt)
res = output.choices[0].text
cmd = res.split("output")[1].split(":")[1].strip()
cmd = cmd + " --kubeconfig /root/kubews/admin.conf"
print(cmd)
print()
output = subprocess.getoutput('sudo ' + cmd)
print(output)
