package(default_visibility = ["//visibility:public"])

load("@grpc_python_dependencies//:requirements.bzl", "requirement")

py_library(
    name = "grpc_health",
    srcs = ["health.py",],
    deps = [
        "//protos/health:health_py_proto",
        requirement("grpcio"),
    ],
)

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
      ":grpc_health",
    ],
)
