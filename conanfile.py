import os
from conans import ConanFile, CMake, tools


class AzureuhttpcConan(ConanFile):
    name = "Azure-uHTTP-C"
    version = "1.0.46"
    license = "https://github.com/Azure/azure-uhttp-c/blob/master/LICENSE"
    url = "https://github.com/bincrafters/conan-azure-uhttp-c"
    description = "The Azure HTTP Library written in C"
    author = "Bincrafters <https://bincrafters.github.io>"
    settings = "os", "compiler", "build_type", "arch"
    requires = "Azure-C-Shared-Utility/1.0.46@bincrafters/stable"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    exports = "LICENSE"
    release_date = "2017-10-20"
    release_dir = "%s-%s" % (name.lower(), release_date)

    def source(self):
        tools.get("https://github.com/Azure/azure-uhttp-c/archive/%s.tar.gz" % self.release_date)

    def configure(self):
        self.options["Azure-C-Shared-Utility"].shared = self.options.shared

    def _insert_magic_lines(self):
        conan_magic_lines='''project(uhttp)
        include(../conanbuildinfo.cmake)
        conan_basic_setup()
        '''
        tools.replace_in_file("CMakeLists.txt", "project(uhttp)", conan_magic_lines)

    def _remove_internal_denpendencies(self):
        tools.replace_in_file("CMakeLists.txt", "include(deps/c-utility/configs/azure_iot_build_rules.cmake)", "")
        tools.replace_in_file("CMakeLists.txt", "add_subdirectory(./deps/c-utility)", "")
        tools.replace_in_file("CMakeLists.txt", "set_platform_files(${CMAKE_CURRENT_LIST_DIR}/deps/c-utility)", "")

    def _build(self):
        cmake = CMake(self)
        cmake.definitions["skip_samples"] = True
        cmake.configure(source_dir=os.getcwd())
        cmake.build()

    def build(self):
        with tools.chdir(self.release_dir):
            self._insert_magic_lines()
            self._remove_internal_denpendencies()
            self._build()

    def package(self):
        self.copy("LICENSE", dst=".", src=".")
        self.copy("*.h", dst="include", src=os.path.join(self.release_dir, "inc"))
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
