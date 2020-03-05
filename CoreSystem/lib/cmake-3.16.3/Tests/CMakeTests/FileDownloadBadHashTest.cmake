if(NOT "/home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeTests" MATCHES "^/")
  set(slash /)
endif()
set(url "file://${slash}/home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeTests/FileDownloadInput.png")
set(dir "/home/ubuntu/environment/DAASystem/CoreSystem/lib/cmake-3.16.3/Tests/CMakeTests/downloads")

file(DOWNLOAD
  ${url}
  ${dir}/file3.png
  TIMEOUT 2
  STATUS status
  EXPECTED_HASH SHA1=5555555555555555555555555555555555555555
  )
