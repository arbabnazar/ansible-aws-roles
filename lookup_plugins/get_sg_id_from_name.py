'''
USAGE:
 - debug:
     msg: "{{ lookup('get_sg_id_from_name', (vpc_region, rds_sg_name)) }}"
'''

from ansible.errors import *
from ansible.plugins.lookup import LookupBase

try:
    import boto
    import boto.ec2
except ImportError:
    raise AnsibleError("get_sg_id_from_name lookup cannot be run without boto installed")

class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):
        region = terms[0][0]
        sg_name = terms[0][1]
        if isinstance(sg_name, basestring):
            sg_name = sg_name
        ec2_conn = boto.ec2.connect_to_region(region)
        sg = ec2_conn.get_all_security_groups(filters={'group_name': sg_name})[0]
        return [sg.id]