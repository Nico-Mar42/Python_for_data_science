import time

s_epoch = time.time()

datetime = time.strftime("%b %d %Y", time.gmtime())
print("Seconds since January 1, 1970:", f"{s_epoch:,.4f}", "or",
      f"{s_epoch:.2e}", "in scientific notation.")
print(datetime, "\n")
