import esp
import gc
import webrepl
import wifi

esp.osdebug(None)
gc.collect()

wifi.connect_wifi()
webrepl.start()

gc.collect()