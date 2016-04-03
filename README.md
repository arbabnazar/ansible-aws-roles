Ansible Roles for AWS Infrastructure Creation
----------------------
There's a series of blog posts that I wrote to go along with these roles. [Check it out!](https://rbgeek.wordpress.com/2016/01/04/aws-infrastructure-creation-with-ansible-part-1/)

The purpose of these Ansible roles are to create the complete infrastructure over AWS using Ansible, which include:

- VPC with public and private subnets in different AZ
- EC2 Key Pair
- Security Groups for EC2,RDS and ELB with tags
- EC2 instance inside the desired AZs
- ELB with SSL support
- RDS instance

I have also written so really small plugins to get the desired information.

Requirement to use these roles:

- Ansible v2.0
- boto
- AWS admin access

Specifically, these are the versions of mentioned software that I am using:

```shell
arbab@ansible2:~$ ansible --version
ansible 2.0.0
  config file =
  configured module search path = Default w/o overrides
arbab@ansible2:~$
arbab@ansible2:~$ python -c 'import boto;print(boto.Version)'
2.38.0
arbab@ansible2:~$
```

Ansible uses python-boto library to call AWS API, and boto needs AWS credentials in order to perform all the functions. There are many ways to configure your AWS credentials. The easiest way is to crate a .boto file under your user home directory:

Then add the following:
```shell
[Credentials]
aws_access_key_id = <your_access_key_here>
aws_secret_access_key = <your_secret_key_here>
```