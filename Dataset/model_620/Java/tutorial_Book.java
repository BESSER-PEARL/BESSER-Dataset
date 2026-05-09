





import java.util.List;
import java.util.ArrayList;

public class tutorial_Book  {

    private String name;
    private String copies;





    private tutorial_Loan tutorial_loan;




    private tutorial_Library tutorial_library;




    private tutorial_Library tutorial_library;


    public tutorial_Book(
        String name,        String copies    ) {
        this.name = name;
        this.copies = copies;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCopies() {
        return copies;
    }

    public void setCopies(String copies) {
        this.copies = copies;
    }

    public tutorial_Loan getTutorial_loan() {
        return tutorial_loan;
    }

    public void setTutorial_loan(tutorial_Loan tutorial_loan) {
        this.tutorial_loan = tutorial_loan;
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