<<<<<<< HEAD

/* simple namespace object interface */

#ifndef NAMESPACEOBJECT_H
#define NAMESPACEOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(PyTypeObject) _PyNamespace_Type;

PyAPI_FUNC(PyObject *) _PyNamespace_New(PyObject *kwds);

#ifdef __cplusplus
}
#endif
#endif /* !NAMESPACEOBJECT_H */
=======

/* simple namespace object interface */

#ifndef NAMESPACEOBJECT_H
#define NAMESPACEOBJECT_H
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(PyTypeObject) _PyNamespace_Type;

PyAPI_FUNC(PyObject *) _PyNamespace_New(PyObject *kwds);

#ifdef __cplusplus
}
#endif
#endif /* !NAMESPACEOBJECT_H */
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
