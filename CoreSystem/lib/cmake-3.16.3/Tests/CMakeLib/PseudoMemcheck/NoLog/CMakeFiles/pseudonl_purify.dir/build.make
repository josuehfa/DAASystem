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
include Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/depend.make

# Include the progress variables for this target.
include Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/progress.make

# Include the compile flags for this target's objects.
include Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/flags.make

Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/ret0.c.o: Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/flags.make
Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/ret0.c.o: Tests/CMakeLib/PseudoMemcheck/NoLog/ret0.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/ret0.c.o"
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/pseudonl_purify.dir/ret0.c.o   -c /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog/ret0.c

Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/ret0.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/pseudonl_purify.dir/ret0.c.i"
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog/ret0.c > CMakeFiles/pseudonl_purify.dir/ret0.c.i

Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/ret0.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/pseudonl_purify.dir/ret0.c.s"
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog && /usr/bin/gcc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog/ret0.c -o CMakeFiles/pseudonl_purify.dir/ret0.c.s

# Object files for target pseudonl_purify
pseudonl_purify_OBJECTS = \
"CMakeFiles/pseudonl_purify.dir/ret0.c.o"

# External object files for target pseudonl_purify
pseudonl_purify_EXTERNAL_OBJECTS =

Tests/CMakeLib/PseudoMemcheck/NoLog/purify: Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/ret0.c.o
Tests/CMakeLib/PseudoMemcheck/NoLog/purify: Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/build.make
Tests/CMakeLib/PseudoMemcheck/NoLog/purify: Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking C executable purify"
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/pseudonl_purify.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/build: Tests/CMakeLib/PseudoMemcheck/NoLog/purify

.PHONY : Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/build

Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/clean:
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog && $(CMAKE_COMMAND) -P CMakeFiles/pseudonl_purify.dir/cmake_clean.cmake
.PHONY : Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/clean

Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/depend:
	cd /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3 && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3 /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3 /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog /home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : Tests/CMakeLib/PseudoMemcheck/NoLog/CMakeFiles/pseudonl_purify.dir/depend

