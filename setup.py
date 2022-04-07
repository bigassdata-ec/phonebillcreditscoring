import setuptools

setuptools.setup(
    name='phonebillcreditscoring',
    version='1.0',
    author="Elton Cheong",
    author_email="youremail@domain.tld",
    url="https://blabla.com",
    data_files = [('', ['phonebillreditscoring/some_schema.json'])],
    include_package_data=True,
    packages=setuptools.find_packages(),
)
