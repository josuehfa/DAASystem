include(Compiler/Intel)
__compiler_intel(C)

string(APPEND CMAKE_C_FLAGS_MINSIZEREL_INIT " -DNDEBUG")
string(APPEND CMAKE_C_FLAGS_RELEASE_INIT " -DNDEBUG")
string(APPEND CMAKE_C_FLAGS_RELWITHDEBINFO_INIT " -DNDEBUG")

set(CMAKE_DEPFILE_FLAGS_C "-MD -MT <OBJECT> -MF <DEPFILE>")

if("x${CMAKE_C_SIMULATE_ID}" STREQUAL "xMSVC")

  if (NOT CMAKE_C_COMPILER_VERSION VERSION_LESS 16.0.0)
    set(CMAKE_C11_STANDARD_COMPILE_OPTION "-Qstd=c11")
    set(CMAKE_C11_EXTENSION_COMPILE_OPTION "-Qstd=c11")
    set(CMAKE_C11_STANDARD__HAS_FULL_SUPPORT ON)
  endif()

  if (NOT CMAKE_C_COMPILER_VERSION VERSION_LESS 12.0)
    set(CMAKE_C90_STANDARD_COMPILE_OPTION "-Qstd=c89")
    set(CMAKE_C90_EXTENSION_COMPILE_OPTION "-Qstd=c89")
    set(CMAKE_C90_STANDARD__HAS_FULL_SUPPORT ON)
    set(CMAKE_C99_STANDARD_COMPILE_OPTION "-Qstd=c99")
    set(CMAKE_C99_EXTENSION_COMPILE_OPTION "-Qstd=c99")
    set(CMAKE_C99_STANDARD__HAS_FULL_SUPPORT ON)
  endif()

else()

  if (NOT CMAKE_C_COMPILER_VERSION VERSION_LESS 15.0.0)
    set(CMAKE_C11_STANDARD_COMPILE_OPTION "-std=c11")
    set(CMAKE_C11_EXTENSION_COMPILE_OPTION "-std=gnu11")
    set(CMAKE_C11_STANDARD__HAS_FULL_SUPPORT ON)
  endif()

  if (NOT CMAKE_C_COMPILER_VERSION VERSION_LESS 12.0)
    set(CMAKE_C90_STANDARD_COMPILE_OPTION "-std=c89")
    set(CMAKE_C90_EXTENSION_COMPILE_OPTION "-std=gnu89")
    set(CMAKE_C90_STANDARD__HAS_FULL_SUPPORT ON)
    set(CMAKE_C99_STANDARD_COMPILE_OPTION "-std=c99")
    set(CMAKE_C99_EXTENSION_COMPILE_OPTION "-std=gnu99")
    set(CMAKE_C99_STANDARD__HAS_FULL_SUPPORT ON)
  endif()

endif()

__compiler_check_default_language_standard(C 12.0 90 15.0.0 11)

set(CMAKE_C_CREATE_PREPROCESSED_SOURCE "<CMAKE_C_COMPILER> <DEFINES> <INCLUDES> <FLAGS> -E <SOURCE> > <PREPROCESSED_SOURCE>")
set(CMAKE_C_CREATE_ASSEMBLY_SOURCE "<CMAKE_C_COMPILER> <DEFINES> <INCLUDES> <FLAGS> -S <SOURCE> -o <ASSEMBLY_SOURCE>")