# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE.md file in the project root for full license information.
"""
Azure AI Vision SDK -- Python Image Analysis Samples

Main entry point for the sample application.
"""

import load_secrets
import platform
import samples
import sys
import os


def print_usage():
    print()
    print(" To run the samples:")
    print()
    print("   python main.py [--key|-k <your-key>] [--endpoint|-e <your-endpoint>]")
    print()
    print(" Where:")
    print("   <your-key> - A computer vision key you get from your Azure portal.")
    print("     It should be a 32-character HEX number.")
    print("   <your-endpoint> - A computer vision endpoint you get from your Azure portal.")
    print("     It should have the form:")
    print("     https://<your-computer-vision-resource-name>.cognitiveservices.azure.com")
    print()
    print(" As an alternative to specifying the above command line arguments, you can define")
    print(" these environment variables: {} and/or {}.".format(load_secrets.ENVIRONMENT_VARIABLE_KEY,
                                                               load_secrets.ENVIRONMENT_VARIABLE_ENDPOINT))
    print()
    print(" To get this usage help, run:")
    print()
    print("   python main.py --help|-h")
    print()

#print(sys.argv)


os.system('cls')
print()
print(" Azure AI Vision SDK - Image Analysis")
print()

for arg in sys.argv:
    if arg in ["--help", "-h"]:
        print_usage()
        sys.exit(0)

if not load_secrets.load_succeeded(sys.argv):
    print_usage()
    sys.exit(1)

samples.image_analysis_sample_analyze(sys.argv)