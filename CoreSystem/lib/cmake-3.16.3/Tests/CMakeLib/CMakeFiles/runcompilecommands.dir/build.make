# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Bootstrap.cmk/cmake

# The command to remove a file.
RM = /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Bootstrap.cmk/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3

# Include any dependencies generated for this target.
include Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/depend.make

# Include the progress variables for this target.
include Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/progress.make

# Include the compile flags for this target's objects.
include Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/flags.make

Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.o: Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/flags.make
Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.o: Tests/CMakeLib/run_compile_commands.cxx
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.o"
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib && /usr/bin/g++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.o -c /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/run_compile_commands.cxx

Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.i"
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/run_compile_commands.cxx > CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.i

Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.s"
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib && /usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/run_compile_commands.cxx -o CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.s

# Object files for target runcompilecommands
runcompilecommands_OBJECTS = \
"CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.o"

# External object files for target runcompilecommands
runcompilecommands_EXTERNAL_OBJECTS =

Tests/CMakeLib/runcompilecommands: Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/run_compile_commands.cxx.o
Tests/CMakeLib/runcompilecommands: Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/build.make
Tests/CMakeLib/runcompilecommands: Source/libCMakeLib.a
Tests/CMakeLib/runcompilecommands: Source/kwsys/libcmsys.a
Tests/CMakeLib/runcompilecommands: Utilities/std/libcmstd.a
Tests/CMakeLib/runcompilecommands: Utilities/cmexpat/libcmexpat.a
Tests/CMakeLib/runcompilecommands: Utilities/cmlibarchive/libarchive/libcmlibarchive.a
Tests/CMakeLib/runcompilecommands: Utilities/cmliblzma/libcmliblzma.a
Tests/CMakeLib/runcompilecommands: Utilities/cmzstd/libcmzstd.a
Tests/CMakeLib/runcompilecommands: Utilities/cmbzip2/libcmbzip2.a
Tests/CMakeLib/runcompilecommands: Utilities/cmcurl/lib/libcmcurl.a
Tests/CMakeLib/runcompilecommands: Utilities/cmzlib/libcmzlib.a
Tests/CMakeLib/runcompilecommands: /usr/lib/x86_64-linux-gnu/libssl.so
Tests/CMakeLib/runcompilecommands: /usr/lib/x86_64-linux-gnu/libcrypto.so
Tests/CMakeLib/runcompilecommands: Utilities/cmjsoncpp/libcmjsoncpp.a
Tests/CMakeLib/runcompilecommands: Utilities/cmlibuv/libcmlibuv.a
Tests/CMakeLib/runcompilecommands: Utilities/cmlibrhash/libcmlibrhash.a
Tests/CMakeLib/runcompilecommands: Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable runcompilecommands"
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/runcompilecommands.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/build: Tests/CMakeLib/runcompilecommands

.PHONY : Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/build

Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/clean:
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib && $(CMAKE_COMMAND) -P CMakeFiles/runcompilecommands.dir/cmake_clean.cmake
.PHONY : Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/clean

Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/depend:
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3 /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3 /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Tests/CMakeLib/CMakeFiles/runcompilecommands.dir/depend

