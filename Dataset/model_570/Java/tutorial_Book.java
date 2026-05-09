





import java.util.List;
import java.util.ArrayList;

public class tutorial_Book  {

    private String copies;
    private String name;





    private tutorial_Member tutorial_member;




    private List<tutorial_Loan> tutorial_loans;




    private tutorial_Library tutorial_library;




    private tutorial_Library tutorial_library;


    public tutorial_Book(
        String copies,        String name    ) {
        this.copies = copies;
        this.name = name;
        this.tutorial_loans = new ArrayList<>();
    }

    public tutorial_Book(
        String copies,        String name        ArrayList<tutorial_Loan> tutorial_loans    ) {
        this.copies = copies;
        this.name = name;
        this.tutorial_loans = tutorial_loans;
    }

    public String getCopies() {
        return copies;
    }

    public void setCopies(String copies) {
        this.copies = copies;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tutorial_Member getTutorial_member() {
        return tutorial_member;
    }

    public void setTutorial_member(tutorial_Member tutorial_member) {
        this.tutorial_member = tutorial_member;
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
    public tutorial_Library getTutorial_library() {
        return tutorial_library;
    }

    public void setTutorial_library(tutorial_Library tutorial_library) {
        this.tutorial_library = tutorial_library;
    }

}