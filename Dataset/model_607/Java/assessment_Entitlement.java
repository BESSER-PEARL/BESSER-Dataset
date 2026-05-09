





import java.util.List;
import java.util.ArrayList;

public class assessment_Entitlement extends Node {






    private assessment_Account assessment_account;




    private List<assessment_Account> assessment_accounts;


    public assessment_Entitlement(
    ) {
        super(
        );
        this.assessment_accounts = new ArrayList<>();
    }

    public assessment_Entitlement(
        ArrayList<assessment_Account> assessment_accounts    ) {
        this.assessment_accounts = assessment_accounts;
    }


    public assessment_Account getAssessment_account() {
        return assessment_account;
    }

    public void setAssessment_account(assessment_Account assessment_account) {
        this.assessment_account = assessment_account;
    }
    public List<assessment_Account> getAssessment_accounts() {
        return assessment_accounts;
    }

    public void addAssessment_account(Assessment_account assessment_account) {
        this.assessment_accounts.add(assessment_account);
    }

}