EVENTSEL_EVENT = 0x00ff
EVENTSEL_UMASK = 0xff00
EVENTSEL_EDGE  = 1<<18
EVENTSEL_PC    = 1<<19
EVENTSEL_ANY   = 1<<21
EVENTSEL_INV   = 1<<23
EVENTSEL_CMASK = 0xff000000

EVMASK = (EVENTSEL_EVENT|EVENTSEL_UMASK|EVENTSEL_EDGE|EVENTSEL_PC|EVENTSEL_ANY|
          EVENTSEL_INV|EVENTSEL_CMASK)

EVENTSEL_ENABLE = 1<<22

MSR_EVNTSEL = 0x186 
MSR_IA32_FIXED_CTR_CTRL = 0x38d
MSR_PEBS_ENABLE = 0x3f1

extra_flags = (
        (EVENTSEL_EDGE, "edge"),
        (EVENTSEL_PC,   "pc"),
        (EVENTSEL_ANY,  "any"),
        (EVENTSEL_INV,  "inv"),
        (EVENTSEL_CMASK, "cmask"))
