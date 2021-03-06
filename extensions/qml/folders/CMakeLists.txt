SET(QT_USE_QTDECLARATIVE ON)

INCLUDE_DIRECTORIES(
    ${QT_INCLUDES}
    )

SET(sourceFiles
    plugin.cpp
    support.cpp
    )

SET(headerFiles
    support.h
    )

SET(QTMOC_SRCS
    support.h
    plugin.h
    )

QT4_WRAP_CPP(QT_MOC_SRCS ${QTMOC_SRCS})

SET(sourceFiles
    ${QTMOC_SRCS}
    ${sourceFiles}
    ${headerFiles}
    )

SET(libs
    ${PLEXY_CORE_LIBRARY}
    )

ADD_LIBRARY(folderview  SHARED ${sourceFiles} ${QT_MOC_SRCS})

#SET_TARGET_PROPERTIES(folderview PROPERTIES DEFINE_SYMBOL Q_DECLARATIVE_EXPORT)

#IF(MINGW)
#    SET_TARGET_PROPERTIES(desktopview PROPERTIES
#        IMPORT_SUFFIX ".lib"
#        IMPORT_PREFIX ""
#        PREFIX ""
#        )
#ENDIF(MINGW)

TARGET_LINK_LIBRARIES(
    folderview
    ${libs}
    )

# Workaround for Ubuntu
IF(${QT_IMPORTS_DIR})
    SET(QT_IMPORTS_DIR ${CMAKE_INSTALL_PREFIX}/lib/qt4/imports/)
ENDIF(${QT_IMPORTS_DIR})

INSTALL(TARGETS folderview DESTINATION lib/qt4/imports/FolderView)
INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/qmldir  DESTINATION lib/qt4/imports/FolderView)
