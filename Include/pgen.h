<<<<<<< HEAD
#ifndef Py_PGEN_H
#define Py_PGEN_H
#ifdef __cplusplus
extern "C" {
#endif


/* Parser generator interface */

extern grammar *meta_grammar(void);

struct _node;
extern grammar *pgen(struct _node *);

#ifdef __cplusplus
}
#endif
#endif /* !Py_PGEN_H */
=======
#ifndef Py_PGEN_H
#define Py_PGEN_H
#ifdef __cplusplus
extern "C" {
#endif


/* Parser generator interface */

extern grammar *meta_grammar(void);

struct _node;
extern grammar *pgen(struct _node *);

#ifdef __cplusplus
}
#endif
#endif /* !Py_PGEN_H */
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
