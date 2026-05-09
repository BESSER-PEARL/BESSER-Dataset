





import java.util.List;
import java.util.ArrayList;

public class tutorial_Library  {

    private String name;





    private tutorial_Member tutorial_member;




    private List<tutorial_Member> tutorial_members;




    private List<tutorial_Loan> tutorial_loans;


    public tutorial_Library(
        String name    ) {
        this.name = name;
        this.tutorial_members = new ArrayList<>();
        this.tutorial_loans = new ArrayList<>();
    }

    public tutorial_Library(
        String name        ArrayList<tutorial_Member> tutorial_members,        ArrayList<tutorial_Loan> tutorial_loans    ) {
        this.name = name;
        this.tutorial_members = tutorial_members;
        this.tutorial_loans = tutorial_loans;
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
    public List<tutorial_Member> getTutorial_members() {
        return tutorial_members;
    }

    public void addTutorial_member(Tutorial_member tutorial_member) {
        this.tutorial_members.add(tutorial_member);
    }
    public List<tutorial_Loan> getTutorial_loans() {
        return tutorial_loans;
    }

    public void addTutorial_loan(Tutorial_loan tutorial_loan) {
        this.tutorial_loans.add(tutorial_loan);
    }

}