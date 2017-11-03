from setuptools import setup, find_packages

description = "This is a set of packages and scripts that provide a simple way for interfacing with the Tanium SOAP API using python or the command line."
setup(
    name='pytan',
    version="2.1.9",
    url='http://tanium.github.io/pytan',
    license='MIT',
    author='Jim Olsen',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: Implementation :: CPython",
        "Natural Language :: English"
    ],
    author_email='jim.olsen@tanium.com',
    description=description,
    long_description=description,
    packages=find_packages("."),
    platforms='any',
    install_requires=[
        'requests>=2.17.3',
        'xmltodict>=0.10.2',
        'pyreadline>=1.5;platform_system=="Windows"'],
    entry_points={
        'console_scripts': ['pytan-approve-saved-action = pytan_pkgs.bin.approve_saved_action:main',
                            'pytan-ask-manual = pytan_pkgs.bin.ask_manual:main',
                            'pytan-ask-parsed = pytan_pkgs.bin.ask_parsed:main',
                            'pytan-ask-saved = pytan_pkgs.bin.ask_saved:main',
                            'pytan-close-session = pytan_pkgs.bin.close_session:main',
                            'pytan-create-action-from-json = pytan_pkgs.bin.create_action_from_json:main',
                            'pytan-create-group = pytan_pkgs.bin.create_group:main',
                            'pytan-create-group-from-json = pytan_pkgs.bin.create_group_from_json:main',
                            'pytan-create-package = pytan_pkgs.bin.create_package:main',
                            'pytan-create-package-from-json = pytan_pkgs.bin.create_package_from_json:main',
                            'pytan-create-saved-question-from-json = pytan_pkgs.bin.create_saved_question_from_json:main',
                            'pytan-create-sensor-from-json = pytan_pkgs.bin.create_sensor_from_json:main',
                            'pytan-create-user = pytan_pkgs.bin.create_user:main',
                            'pytan-create-user-from-json = pytan_pkgs.bin.create_user_from_json:main',
                            'pytan-create-whitelisted-url = pytan_pkgs.bin.create_whitelisted_url:main',
                            'pytan-create-whitelisted-url-from-json = pytan_pkgs.bin.create_whitelisted_url_from_json:main',
                            'pytan-delete-group = pytan_pkgs.bin.delete_group:main',
                            'pytan-delete-package = pytan_pkgs.bin.delete_package:main',
                            'pytan-delete-saved-question = pytan_pkgs.bin.delete_saved_question:main',
                            'pytan-delete-sensor = pytan_pkgs.bin.delete_sensor:main',
                            'pytan-delete-user = pytan_pkgs.bin.delete_user:main',
                            'pytan-delete-whitelisted-url = pytan_pkgs.bin.delete_whitelisted_url:main',
                            'pytan-deploy-action = pytan_pkgs.bin.deploy_action:main',
                            'pytan-get-action = pytan_pkgs.bin.get_action:main',
                            'pytan-get-client = pytan_pkgs.bin.get_client:main',
                            'pytan-get-group = pytan_pkgs.bin.get_group:main',
                            'pytan-get-package = pytan_pkgs.bin.get_package:main',
                            'pytan-get-question = pytan_pkgs.bin.get_question:main',
                            'pytan-get-results = pytan_pkgs.bin.get_results:main',
                            'pytan-get-saved-action = pytan_pkgs.bin.get_saved_action:main',
                            'pytan-get-saved-question = pytan_pkgs.bin.get_saved_question:main',
                            'pytan-get-sensor = pytan_pkgs.bin.get_sensor:main',
                            'pytan-get-session = pytan_pkgs.bin.get_session:main',
                            'pytan-get-setting = pytan_pkgs.bin.get_setting:main',
                            'pytan-get-user = pytan_pkgs.bin.get_user:main',
                            'pytan-get-userrole = pytan_pkgs.bin.get_userrole:main',
                            'pytan-get-whitelisted-url = pytan_pkgs.bin.get_whitelisted_url:main',
                            'pytan-print-sensors = pytan_pkgs.bin.print_sensors:main',
                            'pytan-print-server-info = pytan_pkgs.bin.print_server_info:main',
                            'pytan-pytan-shell = pytan_pkgs.bin.pytan_shell:main',
                            'pytan-stop-action = pytan_pkgs.bin.stop_action:main',
                            'pytan-tsat = pytan_pkgs.bin.tsat:main',
                            'pytan-write-pytan-user-config = pytan_pkgs.bin.write_pytan_user_config:main'
        ]
    }
)
