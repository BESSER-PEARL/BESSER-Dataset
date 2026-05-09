





import java.util.List;
import java.util.ArrayList;

public class tutorial_Member  {

    private String name;





    private tutorial_Loan tutorial_loan;


    public tutorial_Member(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tutorial_Loan getTutorial_loan() {
        return tutorial_loan;
    }

    public void setTutorial_loan(tutorial_Loan tutorial_loan) {
        this.tutorial_loan = tutorial_loan;
    }

}