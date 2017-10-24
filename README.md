[![Travis Status](https://travis-ci.org/bincrafters/conan-azure-uhttp-c.svg?branch=stable%2F1.0.46)](https://travis-ci.org/bincrafters/conan-azure-uhttp-c)
[![Appveyor Status status](https://ci.appveyor.com/api/projects/status/ftmq7dao3m65t4y7/branch/stable/1.0.46?svg=true)](https://ci.appveyor.com/project/BinCrafters/conan-azure-uhttp-c/branch/stable/1.0.46)
[![Download](https://api.bintray.com/packages/bincrafters/public-conan/Azure-uHTTP-C%3Abincrafters/images/download.svg?version=1.0.46%3Astable) ](https://bintray.com/bincrafters/public-conan/Azure-uHTTP-C%3Abincrafters/1.0.46%3Astable/link)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## This repository holds a conan recipe for Azure-uHTTP-C.

[Conan.io](https://conan.io) package for [Azure-uHTTP-C](https://github.com/Azure/azure-uhttp-c) project

The packages generated with this **conanfile** can be found in [Bintray](https://bintray.com/bincrafters/public-conan/Azure-uHTTP-C%3Abincrafters).

## For Users: Use this package

### Basic setup

    $ conan install Azure-uHTTP-C/1.0.46@bincrafters/testing

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    Azure-uHTTP-C/1.0.46@bincrafters/testing

    [generators]
    txt

Complete the installation of requirements for your project running:</small></span>

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they shoudl not be added to the root of the project, nor committed to git.

## For Packagers: Publish this Package

The example below shows the commands used to publish to bincrafters conan repository. To publish to your own conan respository (for example, after forking this git repository), you will need to change the commands below accordingly.

## Build  

This is a header only library, so nothing needs to be built.

## Package

    $ conan create bincrafters/testing

## Add Remote

	$ conan remote add bincrafters "https://api.bintray.com/conan/bincrafters/public-conan"

## Upload

    $ conan upload Azure-uHTTP-C/1.0.46@bincrafters/testing --all -r bincrafters

### License
[MIT](LICENSE)
