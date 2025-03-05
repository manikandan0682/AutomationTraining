# Working with Ansible Templates, Variables, and Facts

## The Scenario

A colleague was the unfortunate victim of a scam email, and their network account was compromised. We have been tasked with deploying a hardened `sudoers` file. We need to create an Ansible template of the `sudoers` file.

We must also create an accompanying playbook in `/home/ansible/lab-template/security.yml` to deploy this template to all servers in the default inventory.



Task list:

* Create a Template `sudoers` file named `/home/ansible/lab-template/hardened.j2` that produces a file with the appropriate output for each host.
* The deployed file should resemble the example file except with the *IP* and *hostnames* customized appropriately.
* Create a playbook in `/home/ansible/lab-template/security.yml` that uses the template module to deploy the template on all servers in the inventory after validating the Syntax of the generated file.
* Run the playbook and ensure the file is correctly deployed.
* The `ansible` user must be able to execute tasks on `localhost.`



## Create a Template *sudoers* File

Create a template file with the following:

```
{% raw %}
%sysops {{ ansible_default_ipv4.address }} = (ALL) ALL
Host_Alias WEBSERVERS = {{ groups['web']|join(' ') }}
Host_Alias DBSERVERS = {{ groups['database']|join(' ') }}
%httpd WEBSERVERS = /bin/su - webuser
%dba DBSERVERS = /bin/su - dbuser
{% endraw %}
```



## Create an inventory file

Create an `inventory` file containing: 

* Three groups (`nodes`, `web`, and `database`)
* A `localhost` entry
* The `nodes` group should contain both nodes
* The `web` group should contain only `node1`
* The `database` group should contain only `node2`



Confirm everything executes successfully. 



## Conclusion

Congratulations on completing the lab!
