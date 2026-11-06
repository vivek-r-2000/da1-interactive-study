import os
import unittest
from bs4 import BeautifulSoup

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
EXAM_PREP_PATH = os.path.join(WORKSPACE, 'Exam_Preparation', 'index.html')

class TestExamPrepFeatures(unittest.TestCase):
    def test_exam_prep_file_exists(self):
        """Exam Preparation portal index.html must exist."""
        self.assertTrue(os.path.exists(EXAM_PREP_PATH), f"File not found at {EXAM_PREP_PATH}")

    def test_endsem_syllabus_coverage(self):
        """All mandated Endsem textbook exercises and papers must be present in the portal."""
        if not os.path.exists(EXAM_PREP_PATH):
            self.skipTest("Exam prep file does not exist yet.")

        with open(EXAM_PREP_PATH, 'r', encoding='utf-8') as fp:
            content = fp.read()

        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text()

        # Mandated Textbook Exercises
        required_exercises = [
            "2.2", "2.7", "2.18", "2.19", "2.20",
            "3.15", "3.17", "3.18", "3.22",
            "4.3", "4.6", "4.10",
            "6.7", "6.19"
        ]
        for ex in required_exercises:
            self.assertIn(ex, text, f"Mandated exercise {ex} missing from Exam Prep portal.")

        # Mandated Endsem Research Papers
        required_papers = [
            "CLARANS",
            "BIRCH",
            "DBSCAN",
            "CHAMELEON",
            "High Utility",
            "Multiple-Level",
            "Quantitative Association Rules"
        ]
        for paper in required_papers:
            self.assertTrue(
                paper.lower() in text.lower(),
                f"Mandated Endsem research paper '{paper}' missing from Exam Prep portal."
            )

    def test_interactive_solvers_present(self):
        """All required interactive numerical solvers must be rendered in DOM with valid elements."""
        if not os.path.exists(EXAM_PREP_PATH):
            self.skipTest("Exam prep file does not exist yet.")

        with open(EXAM_PREP_PATH, 'r', encoding='utf-8') as fp:
            content = fp.read()

        soup = BeautifulSoup(content, 'html.parser')
        
        # Solvers container and key elements
        required_ids = [
            'entropy-solver',
            'buc-solver',
            'apriori-solver',
            'svm-solver',
            'distance-solver',
            'exam-engine'
        ]
        for rid in required_ids:
            self.assertIsNotNone(
                soup.find(id=rid),
                f"Interactive solver section with id='{rid}' missing in Exam Prep portal."
            )

    def test_scientific_calculator_note_and_timer(self):
        """Must include scientific calculator guidance as officially declared by Prof. Reddy."""
        if not os.path.exists(EXAM_PREP_PATH):
            self.skipTest("Exam prep file does not exist yet.")

        with open(EXAM_PREP_PATH, 'r', encoding='utf-8') as fp:
            content = fp.read()

        self.assertIn("Scientific calculators", content)

if __name__ == '__main__':
    unittest.main()
