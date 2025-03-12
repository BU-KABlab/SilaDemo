from sila2.client import SilaClient

# Specify the path to your self-signed CA certificate
ca_cert_path = "server-ca.pem"  # Make sure there are no spaces in the filename

with SilaClient.discover(root_certs=open(ca_cert_path, "rb").read()) as client:
    print(client.GreetingProvider.StartYear.get())
    print(client.GreetingProvider.SayHello(Name="Greg"))
