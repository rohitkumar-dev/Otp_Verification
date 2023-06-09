# OTP Verification

This project demonstrates the implementation of OTP (One-Time Password) verification using Python. OTP verification is commonly used to validate user identity during registration, payment processes, or password reset procedures. In this project, we will create an application that generates a random 6-digit OTP, sends it to the user's email, and prompts the user to enter the OTP for verification.

## Requirements

- Python 3.x
- SMTP library for sending emails (usually included in standard Python distributions)

## Getting Started

1. Clone the repository or download the source code files.
2. Ensure that you have Python 3.x installed on your system.
3. Open a terminal or command prompt and navigate to the project directory.

## Usage

1. Open the `otp_verification.py` file in a text editor.
2. Modify the `sender_email` and `sender_password` variables with your email credentials. Make sure the email account you use has SMTP access enabled.
3. Save the changes and close the file.
4. Run the following command in the terminal or command prompt:

```shell
python otp_verification.py
```

5. The program will prompt you to enter the recipient's email address.
6. An OTP will be generated and sent to the provided email address.
7. Check the email inbox and retrieve the OTP.
8. Enter the OTP in the program when prompted.
9. The program will verify the OTP and display a success or failure message accordingly.

## Customization

You can customize the OTP length and complexity by modifying the `otp_length` and `otp_characters` variables in the `otp_verification.py` file. Additionally, you can customize the email subject and message body in the `send_email` function.

```python
subject = "OTP Verification"
message = f"Your OTP is: {otp}"
```

## Note

Ensure that you have a stable internet connection to send the email. Also, make sure that the SMTP server settings in your email account are correctly configured.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to modify and use the code according to your needs.

## Acknowledgements

The OTP verification project is built using Python and utilizes the SMTP library for sending emails. This project serves as a basic implementation for OTP verification and can be further extended or customized based on specific requirements.
