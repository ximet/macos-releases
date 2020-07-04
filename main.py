import os


nameMap = {
    "5.1": ['Puma', '10.1.1'],
    "5.5": ['Puma', '10.1.5'],
    "6.0.1": ['Jaguar', '10.2'],
    "6.8": ['Jaguar', '10.2.8'],
    "7.0": ['Panther', '10.3.0'],
    "7.9": ['Panther', '10.3.9'],
    "8.0": ['Tiger', '10.4.0'],
    "8.11": ['Tiger', '10.4.11'],
    "9.0": ['Leopard', '10.5.0'],
    "9.8": ['Leopard', '10.5.8'],
    "10.0": ['Snow Leopard', '10.6.0'],
    "10.8": ['Snow Leopard', '10.6.8'],
    "11.0.0": ['Lion', '10.7.0'],
    "11.4.2": ['Lion', '10.7.5'],
    "12.0.0": ['Mountain Lion', '10.8.0'],
    "12.6.0": ['Mountain Lion', '10.8.5'],
    "13.0.0": ['Mavericks', '10.9.0'],
    "13.4.0": ['Mavericks', '10.9.5'],
    "14.0.0": ['Yosemite', '10.10.0'],
    "14.5.0": ['Yosemite', '10.10.5'],
    "15.0.0": ['El Capitan', '10.11.0'],
    "15.6.0": ['El Capitan', '10.11.6'],
    "16.0.0": ['Sierra', '10.12.0'],
    "16.5.0": ['Sierra', '10.12.4'],
    "16.6.0": ['Sierra', '10.12.6'],
    "17.0.0": ['High Sierra', '10.13'],
    "17.5.0": ['High Sierra', '10.13.4'],
    "17.6.0": ['High Sierra', '10.13.5'],
    "17.7.0": ['High Sierra', '10.13.6'],
    "18.0.0": ['Mojave', '10.14'],
    "18.2.0": ['Mojave', '10.14.1'],
    "19.0.0": ['Catalina', '10.15'],
    "19.2.0": ['Catalina', '10.15.2'],
    "19.3.0": ['Catalina', '10.15.3'],
    "19.5.0": ['Catalina', '10.15.5'],
    "19.6.0": ['Catalina', '10.15.6 beta 2'],
    "20.0.0": ['Big Sur', '11.0 beta 1']
}

def getMacOSRelease(release):
    currentRelease = release or os.uname().release
    [name, version] = nameMap.get(currentRelease)
    return (name, version)