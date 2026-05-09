





import java.util.List;
import java.util.ArrayList;

public class assessment_Accounts  {






    private assessment_Application assessment_application;




    private assessment_Account assessment_account;




    private assessment_Application assessment_application;




    private List<assessment_Account> assessment_accounts;


    public assessment_Accounts(
    ) {
        this.assessment_accounts = new ArrayList<>();
    }

    public assessment_Accounts(
        ArrayList<assessment_Account> assessment_accounts    ) {
        this.assessment_accounts = assessment_accounts;
    }


    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }
    public assessment_Account getAssessment_account() {
        return assessment_account;
    }

    public void setAssessment_account(assessment_Account assessment_account) {
        this.assessment_account = assessment_account;
    }
    public assessment_Application getAssessment_application() {
        return assessment_application;
    }

    public void setAssessment_application(assessment_Application assessment_application) {
        this.assessment_application = assessment_application;
    }
    public List<assessment_Account> getAssessment_accounts() {
        return assessment_accounts;
    }

    public void addAssessment_account(Assessment_account assessment_account) {
        this.assessment_accounts.add(assessment_account);
    }

}