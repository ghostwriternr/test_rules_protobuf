package(default_visibility = ["//visibility:public"])

load("@grpc_python_dependencies//:requirements.bzl", "requirement")
load("@org_pubref_rules_protobuf//python:rules.bzl", "py_proto_library")

filegroup(
    name = "health_proto_file",
    srcs = [
        "health.proto",
    ],
)

py_proto_library(
    name = "health_py_proto",
    protos = ["health.proto"],
    with_grpc = True,
    deps = [
        requirement('protobuf'),
    ],
)
