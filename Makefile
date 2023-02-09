ifeq ($(OS), Windows_NT) 
    detected_OS := Windows
else
    detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
endif

BUILDFOLDER := building

ifeq ($(detected_OS), Windows)
EXTTARGET := .pyd
OPTCOMPILE := --compiler=mingw32
MOVECMD := move /Y
MKDIRBUILD := if not exist $(BUILDFOLDER) mkdir $(BUILDFOLDER)
RMFILE := del
RMFOLDER := rmdir /s /q
else
EXTTARGET := .so
OPTCOMPILE := 
MOVECMD := mv
MKDIRBUILD := mkdir -p $(BUILDFOLDER)
RMFILE := rm
RMFOLDER := rm -r
endif

# install ou develop
mode ?= install
ifeq ($(mode), develop) 
    INSTALLOPT := --editable
else
    INSTALLOPT :=  
endif

FORTRANFILES := f90/mod_Cocnstant_ValuesF2PY.f90  \
				f90/mod_Grid3DF2PY_64bit.f90      \
				f90/mod_SkyvaultF2PY.f90          \
				f90/mod_Vegetation_TypesF2PY.f90  \
				f90/mod_Dir_InterceptionF2PY.f90  \
				f90/mod_Hemi_InterceptionF2PY.f90 \
				f90/mod_MicrometeoF2PY.f90        \
				f90/mod_Shortwave_BalanceF2PY.f90 \
				f90/mod_Energy_BalanceF2PY.f90    \
				f90/mod_PhotosynthesisF2PY.f90    \
				f90/mod_MinerPhenoF2PY.f90        \
				f90/prog_RATP.f90


# installation du package Python dans l'interpréteur
install : pyratpmobidiv/pyratp$(EXTTARGET)
	pip install $(INSTALLOPT) .

# copie dans les source python et simplifie le nom de la librairie
pyratpmobidiv/pyratp$(EXTTARGET): pyratp.*$(EXTTARGET)
	$(MOVECMD) pyratp.*$(EXTTARGET) pyratpmobidiv/pyratp$(EXTTARGET)

# compilation de la librairie	
pyratp.*$(EXTTARGET): pyratp.pyf
	$(MKDIRBUILD)
	f2py -c --build-dir $(BUILDFOLDER) $(OPTCOMPILE) --fcompiler=gnu95 pyratp.pyf $(FORTRANFILES)

# création de l'entete
pyratp.pyf: 
	f2py -m pyratp --overwrite-signature -h $@ $(FORTRANFILES)

clean:
	$(RMFILE) pyratp.pyf
	$(RMFOLDER) $(BUILDFOLDER)
