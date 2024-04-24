import rpyc

conn = rpyc.connect("localhost", 12345)

# Submit a Covid report
response = conn.root.submit_report("12345678901", "John Doe", "Jane Doe", "123 Main St", "Demam, Batuk")
print("Response from server:", response)
