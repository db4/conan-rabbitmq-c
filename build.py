from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(build_policy="missing")
    builder.visual_runtimes = ["MD", "MDd"]
    builder.add_common_builds(shared_option_name="rabbitmq-c:shared", pure_c=False)
    builder.run()

