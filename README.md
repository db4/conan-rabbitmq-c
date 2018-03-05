# conan-rabbitmq-c

[Conan.io](https://conan.io) package for [RabbitMQ C/C++ library](https://github.com/alanxz/rabbitmq-c)

| Appveyor | Travis |
|-----------|--------|
|[![Build Status](https://ci.appveyor.com/api/projects/status/github/db4/conan-rabbitmq-c?branch=master&svg=true)](https://ci.appveyor.com/project/db4/conan-rabbitmq-c)|[![Build Status](https://travis-ci.org/db4/conan-rabbitmq-c.svg?branch=master)](https://travis-ci.org/db4/conan-rabbitmq-c)|

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload rabbitmq-c/0.6.0@dbely/stable --all

## Reuse the packages

### Basic setup

    $ conan install rabbitmq-c/0.6.0@dbely/stable

### Project setup

If you handle multiple dependencies in your project, it would be better to add a *conanfile.txt*

    [requires]
    rabbitmq-c/0.6.0@dbely/stable

    [generators]
    txt
    cmake


