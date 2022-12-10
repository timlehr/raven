from esprun import ESPAppProduct


class RavenProduct(ESPAppProduct):
    @property
    def name(self):
        return "Raven"

    @property
    def package_name(self) -> str:
        return "raven"

    @property
    def info_plist_filenames(self):
        return []

    @property
    def maintain_changelog(self):
        return False

    @property
    def build_schemes(self) -> dict[str, tuple[str, list[str]]]:
        return {"raven": (f"{self.build_root}/raven.xcodeproj", ["Raven OTIO Viewer.app"])}

    @property
    def architecture(self) -> str:
        return "$(ARCHS_STANDARD)"

    @property
    def munki_category(self):
        return "Editorial"

    @property
    def munki_description(self):
        return "Experimental OpenTimelineIO Viewer"

    @property
    def munki_minimum_os_version(self):
        return "11.0"

    @property
    def package_identifier(self) -> str:
        return f"com.opentimelineio.{self.package_name}.pkg"

    @property
    def munki_developer(self):
        return "OpenTimelineIO Community"

    def run_pre_build(self, **kwargs):
        # run cmake to setup xcode project
        self._exec_cmd(
            [
                "/Applications/CMake.app/Contents/bin/cmake",  # HACK: horrible hardcode until we upgrade our cmake to 3.20+
                str(self.repo_root),
                "-G",
                "Xcode",
                "-T",
                "buildsystem=12",
                "-DCMAKE_CXX_COMPILER=/usr/bin/clang++",
                "-DCMAKE_C_COMPILER=/usr/bin/clang",
            ],
            cwd=str(self.build_root),
        )
        return self.build_root


# important for discoverability by ESPReleaseManager
PRODUCT_CLASS = RavenProduct
