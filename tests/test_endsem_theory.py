import os
import unittest
from bs4 import BeautifulSoup

WORKSPACE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
THEORY_PATH = os.path.join(WORKSPACE, 'Study_Material', 'endsem_master_theory.html')

class TestEndsemTheoryMaster(unittest.TestCase):
    def setUp(self):
        self.assertTrue(os.path.exists(THEORY_PATH), f"File {THEORY_PATH} does not exist.")
        with open(THEORY_PATH, 'r', encoding='utf-8') as f:
            self.html = f.read()
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.text = self.soup.get_text()

    def test_file_substantial_content(self):
        """File must be substantial (>80,000 bytes) with comprehensive theory."""
        size = os.path.getsize(THEORY_PATH)
        self.assertGreater(size, 80000, f"File size is only {size} bytes, expected >80KB")

    def test_all_blueprint_topics_present(self):
        """All 10 blueprint topics, calculator guide, and cross-chapter synthesis must exist as sections."""
        required_topics = [
            "Chapter 1: Introduction",
            "Chapter 2: Data Preprocessing",
            "Chapter 3: Data Warehousing",
            "Chapter 4: Pattern Mining",
            "Chapter 5: Advanced Pattern Mining",
            "Chapter 6: Classification Basic",
            "Chapter 7: Advanced Classification",
            "Chapter 8: Cluster Analysis",
            "Topic 9: Overview of Deep Learning",
            "Topic 10: Advances in Clustering, Outlier Analysis",
            "Scientific Calculator",
            "Cross-Chapter Synthesis"
        ]
        for topic in required_topics:
            self.assertTrue(
                topic.lower() in self.text.lower(),
                f"Topic '{topic}' missing from Endsem Theory Master Guide."
            )

    def test_all_seven_endsem_papers_present(self):
        """All 7 mandated Endsem research papers must be thoroughly covered."""
        papers = [
            "Multiple-Level Association Rules",
            "Quantitative Association Rules",
            "High Utility",
            "CLARANS",
            "BIRCH",
            "DBSCAN",
            "CHAMELEON"
        ]
        for p in papers:
            self.assertTrue(
                p.lower() in self.text.lower(),
                f"Mandated paper '{p}' missing from Endsem Theory Master Guide."
            )

    def test_all_fourteen_textbook_exercises_present(self):
        """All 14 mandated textbook exercises must be present with step-by-step solutions."""
        exercises = [
            "2.2", "2.7", "2.18", "2.19", "2.20",
            "3.15", "3.17", "3.18", "3.22",
            "4.3", "4.6", "4.10",
            "6.7", "6.19"
        ]
        for ex in exercises:
            self.assertIn(ex, self.text, f"Textbook exercise {ex} missing from theory guide.")

    def test_low_attention_span_friendly_elements(self):
        """Must include quick takeaways, analogies, exam traps, and live search for low-attention learners."""
        # TL;DR or Quick Takeaway callouts
        self.assertTrue(
            "tldr" in self.html.lower() or "takeaway" in self.html.lower(),
            "Missing TL;DR / Quick Takeaway chunking callouts."
        )
        # Real-World Analogies / Intuition
        self.assertTrue(
            "analogy" in self.html.lower() or "intuition" in self.html.lower(),
            "Missing real-world analogies / intuition sections."
        )
        # Professor's Exam Traps
        self.assertTrue(
            "trap" in self.html.lower() or "red flag" in self.html.lower(),
            "Missing Professor's Exam Trap / Pitfall callouts."
        )
        # Live Search input
        search_input = self.soup.find('input', id='theory-search-input')
        self.assertIsNotNone(search_input, "Missing #theory-search-input element for instant filtering.")

if __name__ == '__main__':
    unittest.main()
