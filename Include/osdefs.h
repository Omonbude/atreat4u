<<<<<<< HEAD
#ifndef Py_OSDEFS_H
#define Py_OSDEFS_H
#ifdef __cplusplus
extern "C" {
#endif


/* Operating system dependencies */

/* Mod by chrish: QNX has WATCOM, but isn't DOS */
#if !defined(__QNX__)
#if defined(MS_WINDOWS) || defined(__BORLANDC__) || defined(__WATCOMC__) || defined(__DJGPP__)
#define SEP L'\\'
#define ALTSEP L'/'
#define MAXPATHLEN 256
#define DELIM L';'
#endif
#endif

/* Filename separator */
#ifndef SEP
#define SEP L'/'
#endif

/* Max pathname length */
#ifdef __hpux
#include <sys/param.h>
#include <limits.h>
#ifndef PATH_MAX
#define PATH_MAX MAXPATHLEN
#endif
#endif

#ifndef MAXPATHLEN
#if defined(PATH_MAX) && PATH_MAX > 1024
#define MAXPATHLEN PATH_MAX
#else
#define MAXPATHLEN 1024
#endif
#endif

/* Search path entry delimiter */
#ifndef DELIM
#define DELIM L':'
#endif

#ifdef __cplusplus
}
#endif
#endif /* !Py_OSDEFS_H */
=======
#ifndef Py_OSDEFS_H
#define Py_OSDEFS_H
#ifdef __cplusplus
extern "C" {
#endif


/* Operating system dependencies */

/* Mod by chrish: QNX has WATCOM, but isn't DOS */
#if !defined(__QNX__)
#if defined(MS_WINDOWS) || defined(__BORLANDC__) || defined(__WATCOMC__) || defined(__DJGPP__)
#define SEP L'\\'
#define ALTSEP L'/'
#define MAXPATHLEN 256
#define DELIM L';'
#endif
#endif

/* Filename separator */
#ifndef SEP
#define SEP L'/'
#endif

/* Max pathname length */
#ifdef __hpux
#include <sys/param.h>
#include <limits.h>
#ifndef PATH_MAX
#define PATH_MAX MAXPATHLEN
#endif
#endif

#ifndef MAXPATHLEN
#if defined(PATH_MAX) && PATH_MAX > 1024
#define MAXPATHLEN PATH_MAX
#else
#define MAXPATHLEN 1024
#endif
#endif

/* Search path entry delimiter */
#ifndef DELIM
#define DELIM L':'
#endif

#ifdef __cplusplus
}
#endif
#endif /* !Py_OSDEFS_H */
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
