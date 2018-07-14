package(default_visibility = ["//visibility:public"])

py_library(
    name = "grpc_health",
    srcs = ["health.py",],
    deps = [
        "//protos/health:health_py_proto",
    ],
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
      ":grpc_health",
    ],
)
