def make_table(m):
    return [[] for _ in range(m)]

def hash_basic(s):
    return sum(ord(c) for c in s)

def put(t, key, value):
    index = hash_basic(key) % len(t)
    bucket = t[index]
    for i, (k, _) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return
    bucket.append((key, value))

def get(t, key):
    index = hash_basic(key) % len(t)
    bucket = t[index]
    for k, v in bucket:
        if k == key:
            return v
    return None

def has_key(t, key):
    index = hash_basic(key) % len(t)
    bucket = t[index]
    for k, _ in bucket:
        if k == key:
            return True
    return False

def size(t):
    return sum(len(bucket) for bucket in t)

if __name__ == "__main__":
    t = make_table(5)
    put(t, "B123", "Data Structures")
    print(get(t, "B123"))
    print(size(t))