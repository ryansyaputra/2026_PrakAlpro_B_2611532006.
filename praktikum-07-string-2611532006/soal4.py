phone = "08123456789"
masked = phone[:4] + "*" * 4 + phone[-4:]
print(masked)
