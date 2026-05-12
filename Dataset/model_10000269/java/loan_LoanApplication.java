





import java.util.List;
import java.util.ArrayList;

public class loan_LoanApplication  {

    private float interestRate;
    private None type;
    private String submissionTime;
    private String userID;
    private float amount;
    private None status;
    private int term;
    private String applicationID;



    public loan_LoanApplication(
        float interestRate,        None type,        String submissionTime,        String userID,        float amount,        None status,        int term,        String applicationID    ) {
        this.interestRate = interestRate;
        this.type = type;
        this.submissionTime = submissionTime;
        this.userID = userID;
        this.amount = amount;
        this.status = status;
        this.term = term;
        this.applicationID = applicationID;
    }


    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
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
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public int getTerm() {
        return term;
    }

    public void setTerm(int term) {
        this.term = term;
    }
    public String getApplicationid() {
        return applicationID;
    }

    public void setApplicationid(String applicationID) {
        this.applicationID = applicationID;
    }


}