# 🖥️ machineQuestioning
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

## Περιγραφή
Το **machineQuestioning** είναι μια διαδραστική εφαρμογή κουίζ που εστιάζει στη θεωρία της Μηχανικής Μάθησης. Περιλαμβάνει 82 προσεκτικά επιλεγμένες ερωτήσεις χωρισμένες σε 3 βασικά κεφάλαια (Εισαγωγή, k-NN & Δέντρα Απόφασης, Τεχνητά Νευρωνικά Δίκτυα). 

Το UI είναι εμπνευσμένο από τις ρετρό οθόνες τερματικού (terminal style) με νέον πράσινα χρώματα, προσφέροντας μια νοσταλγική hacker αισθητική.

## Χαρακτηριστικά
* **82 Θεωρητικές Ερωτήσεις:** Καλύπτουν μεγάλο φάσμα της θεωρίας Μηχανικής Μάθησης.
* **Άμεση Επεξήγηση:** Κάθε απάντηση (σωστή ή λάθος) συνοδεύεται από σύντομη και περιεκτική εξήγηση.
* **Κατηγοριοποίηση (Filtering):** Δυνατότητα επιλογής συγκεκριμένου κεφαλαίου μέσω της πλευρικής μπάρας (Sidebar).
* **Αλγόριθμος Fisher-Yates:** Οι ερωτήσεις ανακατεύονται με τυχαία σειρά κάθε φορά που ξεκινάει ένα κουίζ ή αλλάζει κατηγορία.
* **Βάση Δεδομένων:** Όλες οι ερωτήσεις αποθηκεύονται και ανακτώνται δυναμικά από μια τοπική βάση `SQLite`, διατηρώντας το backend API καθαρό.
* **Retro UI:** Dark theme με monospace γραμματοσειρές και hover glow effects.

## Εγκατάσταση και Εκτέλεση (Local Setup)

Ακολούθησε τα παρακάτω βήματα για να τρέξεις την εφαρμογή τοπικά στον υπολογιστή σου.

**1. Κλωνοποίηση του αποθετηρίου (Clone the repo):**
```bash
git clone [https://github.com/simigdalius/machineQuestioning.git](https://github.com/simigdalius/machineQuestioning.git)
cd machineQuestioning
