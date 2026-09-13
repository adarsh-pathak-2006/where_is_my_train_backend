def station_cache_key(pageno):
    return f"station_caches_page:{pageno}"

def train_list_cache_key(pageno):
    return f"train_list_key_page:{pageno}"

def train_all_station_cache_key(train_id):
    return f"train_stations_key_trainid:{train_id}"