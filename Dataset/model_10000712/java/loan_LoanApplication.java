





import java.util.List;
import java.util.ArrayList;

public class loan_LoanApplication  {

    private String applicationID;
    private String userID;
    private None type;
    private String submissionTime;
    private int term;
    private float interestRate;
    private None status;
    private float amount;





    private Profile profile;


    public loan_LoanApplication(
        String applicationID,        String userID,        None type,        String submissionTime,        int term,        float interestRate,        None status,        float amount    ) {
        this.applicationID = applicationID;
        this.userID = userID;
        this.type = type;
        this.submissionTime = submissionTime;
        this.term = term;
        this.interestRate = interestRate;
        this.status = status;
        this.amount = amount;
    }


    public String getApplicationid() {
        return applicationID;
    }

    public void setApplicationid(String applicationID) {
        this.applicationID = applicationID;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getSubmissiontime() {
        return submissionTime;
    }

    public void setSubmissiontime(String submissionTime) {
        this.submissionTime = submissionTime;
    }
    public int getTerm() {
        return term;
    }

    public void setTerm(int term) {
        this.term = term;
    }
    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }

    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }

}