SET(PREFIX_ext_fftw3 "${EXTPREFIX}" )
ExternalProject_Add( ext_fftw3
        DOWNLOAD_DIR ${EXTERNALS_DOWNLOAD_DIR}
     	URL http://www.fftw.org/fftw-3.3.7.tar.gz
        URL_MD5 0d5915d7d39b3253c1cc05030d79ac47

        PATCH_COMMAND ${PATCH_COMMAND} -p1 -i ${CMAKE_CURRENT_SOURCE_DIR}/patch_mingw.patch

        INSTALL_DIR ${PREFIX_ext_fftw3}
        CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${PREFIX_ext_fftw3} -DCMAKE_BUILD_TYPE=${GLOBAL_BUILD_TYPE} ${GLOBAL_PROFILE}  

        UPDATE_COMMAND ""
)
