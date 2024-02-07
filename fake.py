from faker import Faker
fake = Faker()
print(fake.name(),"\n", fake.text())
for i in range(10):
    print(i," ",fake.name(),"\n","||" "Their address ", '---',fake.address())


print("Fake IP address is: ")
print(fake.ipv4_private())
