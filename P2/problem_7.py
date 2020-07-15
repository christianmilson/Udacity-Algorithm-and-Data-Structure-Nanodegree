# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.head = RouteTrieNode('root handler')

    def insert(self, routes, handler=None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        node = self.head
        for route in routes:
            node.insert(route)
            node = node.children[route]

        node.handler = handler

    def find(self, routes):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        node = self.head
        for route in routes:
            if (route in node.children):
                node = node.children[route]
            else:
                return None

        return node.handler

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler=None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, route):
        # Insert the node as before
        if (route not in self.children):
            self.children[route] = RouteTrieNode()
        

# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, base_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie    = RouteTrie()
        self.base_handler = base_handler
        self.not_found = not_found_handler

    def add_handler(self, routes, handler=None) -> None:
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.trie.insert(self.split_path(routes), handler)

    def lookup(self, routes) -> str:
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        routes = self.split_path(routes)

        if (len(routes) < 1):
            return self.base_handler

        handler = self.trie.find(routes)

        if (handler is None):
            return self.not_found

        return handler


    def split_path(self, routes) -> list:
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [route for route in routes.split("/") if route != '']

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("")) # should print 'root found handler' or None if you did not implement one
print(router.lookup("home/about")) # should print 'about handler' or None if you did not implement one