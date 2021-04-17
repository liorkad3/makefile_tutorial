TOPTARGETS := all clean

SUBDIRS:=$(wildcard */.)
EXCLUDE_DIRS=py_blur/.
SUBDIRS:=$(filter-out $(EXCLUDE_DIRS),$(SUBDIRS))

$(info $$SUBDIRS is [${SUBDIRS}])

$(TOPTARGETS): $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(MAKECMDGOALS)

.PHONY: $(TOPTARGETS) $(SUBDIRS)