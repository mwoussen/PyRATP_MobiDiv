from setuptools import setup

setup(
    name="PyRATP_MobiDiv",
    version="0.0.0",
    description="Fork of PyRATP",
    url="https://github.com/mwoussen/PyRATP_MobiDiv",
    author="Maurane Woussen",
    author_email="maurin.woussen@inrae.fr",
    packages=["pyratpmobidiv", "pyratpmobidiv_wralea"],
    package_dir={"pyratpmobidiv" : "pyratpmobidiv", "pyratpmobidiv_wralea" : "pyratpmobidiv_wralea"},
    include_package_data = True,
    package_data = {'' : ['*.pyd', '*.so'],}
)