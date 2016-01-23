from jinja2.utils import soft_unicode

'''
USAGE:
 - debug:
     msg: "{{ ec2.results | get_ec2_info('id') }}"

Some useful ec2 keys:
id
dns_name
public_ip
private_ip
'''

class FilterModule(object):
    def filters(self):
        return {
            'get_ec2_info': get_ec2_info,
        }

def get_ec2_info(list, ec2_key):
    ec2_info = []
    for item in list:
        for ec2 in item['instances']:
            ec2_info.append(ec2[ec2_key])
    return ec2_info
   