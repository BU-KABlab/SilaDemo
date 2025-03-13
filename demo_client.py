from sila2.client import SilaClient

# Specify the path to your self-signed CA certificate
ca_cert_path = "server-ca.pem"  # Make sure there are no spaces in the filename
while True:
    try:
        with SilaClient.discover(root_certs=open(ca_cert_path, "rb").read()) as client:
            features = client.SiLAService.ImplementedFeatures.get()
            parsed_features = [f.split("/")[-2] for f in features]
            print("Features implemented by the server:")
            for i, (feature, parsed) in enumerate(zip(features, parsed_features), 1):
                print(f"  {i}. {parsed} ({feature})")

            selection = input("Enter feature number (or q to quit): ")
            if selection.lower() == "q":
                break

            try:
                index = int(selection) - 1
                if 0 <= index < len(features):
                    feature = features[index]
                    parsed_feature = parsed_features[index]
                    print(f"Selected: {parsed_feature} ({feature})")
                    print("Available commands:")
                    # Note: You need to define these variables properly
                else:
                    print("Invalid feature number.")
            except ValueError:
                print("Please enter a valid number or 'q' to quit.")

    except Exception as e:
        print(f"Error: {e}")
        break
    finally:
        input("Press Enter to continue...")
