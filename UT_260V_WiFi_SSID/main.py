from change_wifi_name import *
from reconnect_wifi import *
from common_para import *

def run_all():
    print_current_time()
    router_tenda()
    reconnect_wifi()

if __name__ == '__main__':
    run_all()
