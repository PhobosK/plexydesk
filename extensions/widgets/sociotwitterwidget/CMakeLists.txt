#ADD_SUBDIRECTORY(youtube)

INCLUDE_DIRECTORIES(
    ${QT_INCLUDES}
    ${QT_QTOPENGL_INCLUDE_DIR}
    ${QT_QTNETWORK_INCLUDE_DIR}
    ${QT_QTTEST_INCLUDE_DIR}
    )

SET(sourceFiles
    sociotwitter.cpp
    sociotwitterinterface.cpp
    sociotwitterwidget.cpp
    )

SET(headerFiles
    sociotwitter.h
    sociotwitterinterface.h
    sociotwitterwidget.h
    )

SET(QTMOC_SRCS
    sociotwitter.h
    sociotwitterinterface.h
    sociotwitterwidget.h
    )

QT4_WRAP_CPP(QT_MOC_SRCS ${QTMOC_SRCS})

SET(sourceFiles
    ${sourceFiles}
    ${headerFiles}
    )

SET(libs
    ${QT_QTGUI_LIBRARY}
    ${OPENGL_LIBRARIES}
    ${QT_QTCORE_LIBRARY}
    ${QT_QTOPENGL_LIBRARY}
    )

ADD_LIBRARY(sociotweets SHARED ${sourceFiles} ${QT_MOC_SRCS})

TARGET_LINK_LIBRARIES(
    sociotweets
    qtviz
    ${libs}
    )

INSTALL(TARGETS sociotweets DESTINATION lib/plexyext)
INSTALL(FILES sociotweets.desktop DESTINATION share/plexy/ext/groups)
