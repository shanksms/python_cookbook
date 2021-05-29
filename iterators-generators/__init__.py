"""
When the Python yield statement is hit,
the program suspends function execution and returns the yielded value to the caller.
(In contrast, return stops function execution completely.)
When a function is suspended, the state of that function is saved.
 This includes any variable bindings local to the generator, the instruction pointer,
 the internal stack, and any exception handling.

This allows you to resume function execution whenever you call one of the generator’s methods.
 In this way, all function evaluation picks back up right after yield.
 You can see this in action by using multiple Python yield statements:
"""