import importlib.util
import unittest

class TestPippyChatbotImports(unittest.TestCase):

    def verify_library_installed(self, library_name):
        """ Test if specified library is installed """
        library_installed = importlib.util.find_spec(library_name) is not None
        self.assertTrue(library_installed, f"{library_name} library is not installed")

    def test_library_streamlit_installed(self):
        self.verify_library_installed("streamlit")

    def test_library_pypdf_installed(self):
        self.verify_library_installed("pypdf")

    def test_library_ipywidgets_installed(self):
        self.verify_library_installed("ipywidgets")

    def test_library_langchain_installed(self):
        self.verify_library_installed("langchain")

    def test_library_dominodatalab_data_installed(self):
        self.verify_library_installed("domino_data")

    def test_library_pinecone_client_installed(self):
        self.verify_library_installed("pinecone")

if __name__ == '__main__':
    unittest.main()