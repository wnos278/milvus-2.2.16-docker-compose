from pymilvus import connections, utility

# connect command
connections.connect("default", host="<host_ip>", port=19530)

# check connection
if not utility.has_collection("gpu_collection"):
    print("Connecting Milvus success!")

