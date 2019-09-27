<<<<<<< HEAD
#ifndef Py_STRCMP_H
#define Py_STRCMP_H

#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(int) PyOS_mystrnicmp(const char *, const char *, Py_ssize_t);
PyAPI_FUNC(int) PyOS_mystricmp(const char *, const char *);

#ifdef MS_WINDOWS
#define PyOS_strnicmp strnicmp
#define PyOS_stricmp stricmp
#else
#define PyOS_strnicmp PyOS_mystrnicmp
#define PyOS_stricmp PyOS_mystricmp
#endif

#ifdef __cplusplus
}
#endif

#endif /* !Py_STRCMP_H */
=======
#ifndef Py_STRCMP_H
#define Py_STRCMP_H

#ifdef __cplusplus
extern "C" {
#endif

PyAPI_FUNC(int) PyOS_mystrnicmp(const char *, const char *, Py_ssize_t);
PyAPI_FUNC(int) PyOS_mystricmp(const char *, const char *);

#ifdef MS_WINDOWS
#define PyOS_strnicmp strnicmp
#define PyOS_stricmp stricmp
#else
#define PyOS_strnicmp PyOS_mystrnicmp
#define PyOS_stricmp PyOS_mystricmp
#endif

#ifdef __cplusplus
}
#endif

#endif /* !Py_STRCMP_H */
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
