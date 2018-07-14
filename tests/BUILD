package(default_visibility = ["//visibility:public"])

py_test(
    name = "print_bottle_test",
    srcs = ["print_bottle_test.py",],
    main = "print_bottle_test.py",
    size = "small",
    deps = [
        "//src/py_health:grpc_health",
    ],
    imports = ["../"],
)
