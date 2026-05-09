





import java.util.List;
import java.util.ArrayList;

public class tutorial_Member  {

    private String name;





    private List<tutorial_Book> tutorial_books;




    private tutorial_Library tutorial_library;




    private List<tutorial_Loan> tutorial_loans;




    private tutorial_Library tutorial_library;




    private tutorial_Loan tutorial_loan;


    public tutorial_Member(
        String name    ) {
        this.name = name;
        this.tutorial_books = new ArrayList<>();
        this.tutorial_loans = new ArrayList<>();
    }

    public tutorial_Member(
        String name        ArrayList<tutorial_Book> tutorial_books,        ArrayList<tutorial_Loan> tutorial_loans    ) {
        this.name = name;
        this.tutorial_books = tutorial_books;
        this.tutorial_loans = tutorial_loans;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tutorial_Book> getTutorial_books() {
        return tutorial_books;
    }

    public void addTutorial_book(Tutorial_book tutorial_book) {
        this.tutorial_books.add(tutorial_book);
    }
    public tutorial_Library getTutorial_library() {
        return tutorial_library;
    }

    public void setTutorial_library(tutorial_Library tutorial_library) {
        this.tutorial_library = tutorial_library;
    }
    public List<tutorial_Loan> getTutorial_loans() {
        return tutorial_loans;
    }

    public void addTutorial_loan(Tutorial_loan tutorial_loan) {
        this.tutorial_loans.add(tutorial_loan);
    }
    public tutorial_Library getTutorial_library() {
        return tutorial_library;
    }

    public void setTutorial_library(tutorial_Library tutorial_library) {
        this.tutorial_library = tutorial_library;
    }
    public tutorial_Loan getTutorial_loan() {
        return tutorial_loan;
    }

    public void setTutorial_loan(tutorial_Loan tutorial_loan) {
        this.tutorial_loan = tutorial_loan;
    }

}