ifeq ($(OS),Windows_NT)
    os := win
    SCRIPT_EXT := .bat
    SHELL_CMD := cmd /C
else
    os := nix
    SCRIPT_EXT := .sh
    SHELL_CMD := bash
endif

helpers = @$(SHELL_CMD) helpers$(SCRIPT_EXT) $1

clean qa style: helpers$(SCRIPT_EXT)

clean:
	$(call helpers,clean)

qa:
	$(call helpers,qa)

style:
	$(call helpers,style)

.PHONY: clean qa style