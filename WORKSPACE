git_repository(
    name = "io_bazel_rules_python",
    remote = "https://github.com/bazelbuild/rules_python.git",
    commit = "8b5d0683a7d878b28fffe464779c8a53659fc645",
)

load("@io_bazel_rules_python//python:pip.bzl", "pip_repositories", "pip_import")

pip_repositories()
pip_import(
    name = "grpc_python_dependencies",
    requirements = "//:requirements.bazel.txt",
)

load("@grpc_python_dependencies//:requirements.bzl", "pip_install")
pip_install()

git_repository(
  name = "org_pubref_rules_protobuf",
  remote = "https://github.com/ghostwriternr/rules_protobuf",
  tag = "v0.8.2.1-alpha",
)

load("@org_pubref_rules_protobuf//python:rules.bzl", "py_proto_repositories")
py_proto_repositories()
