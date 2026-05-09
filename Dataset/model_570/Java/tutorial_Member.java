





import java.util.List;
import java.util.ArrayList;

public class tutorial_Member  {

    private String name;





    private List<tutorial_Loan> tutorial_loans;




    private tutorial_Loan tutorial_loan;


    public tutorial_Member(
        String name    ) {
        this.name = name;
        this.tutorial_loans = new ArrayList<>();
    }

    public tutorial_Member(
        String name        ArrayList<tutorial_Loan> tutorial_loans    ) {
        this.name = name;
        this.tutorial_loans = tutorial_loans;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tutorial_Loan> getTutorial_loans() {
        return tutorial_loans;
    }

    public void addTutorial_loan(Tutorial_loan tutorial_loan) {
        this.tutorial_loans.add(tutorial_loan);
    }
    public tutorial_Loan getTutorial_loan() {
        return tutorial_loan;
    }

    public void setTutorial_loan(tutorial_Loan tutorial_loan) {
        this.tutorial_loan = tutorial_loan;
    }

}