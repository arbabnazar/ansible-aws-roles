from jinja2.utils import soft_unicode

'''
USAGE:
 - debug:
     msg: "{{ vpc.subnets | get_public_subnets_ids('Type','Public') }}"
'''

class FilterModule(object):
    def filters(self):
        return {
            'get_public_subnets_ids': get_public_subnets_ids,
        }

def get_public_subnets_ids(list, tag_key, tag_value):
    subnets_ids = []
    for item in list:
        for key, value in item['resource_tags'].iteritems():
            if key == tag_key and value == tag_value:
                subnets_ids.append(item['id'])

    return subnets_ids