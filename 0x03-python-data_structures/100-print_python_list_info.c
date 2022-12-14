#include <python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print the length of a python list
 * @p: pointer to a PyObject
 */
void print_python_list_info(PyObject *p)
{
	size_t i = 0;
	size_t length = 0;
	PyListObject *Plist = (PyListObject *)p;

	length = PyList_Size(p);
	printf("[*] Size of the Python List = %lu\n", length);
	printf("[*] Allocated = %lu\n", Plist->allocated);
	for (i = 0; i < length; i++)
		printf("Element %lu: %s\n", i, Py_TYPE(Plist->ob_item[i])->tp_name);
}
