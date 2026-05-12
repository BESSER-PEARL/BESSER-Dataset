





import java.util.List;
import java.util.ArrayList;

public class loan_Loan  {

    private float interestRate;
    private float amount;
    private int term;
    private None status;
    private String submissionTime;
    private String loanID;
    private String userID;
    private None type;





    private loan_LoanApplication loan_loanapplication;


    public loan_Loan(
        float interestRate,        float amount,        int term,        None status,        String submissionTime,        String loanID,        String userID,        None type    ) {
        this.interestRate = interestRate;
        this.amount = amount;
        this.term = term;
        this.status = status;
        this.submissionTime = submissionTime;
        this.loanID = loanID;
        this.userID = userID;
        this.type = type;
    }


    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public int getTerm() {
        return term;
    }

    public void setTerm(int term) {
        this.term = term;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public String getSubmissiontime() {
        return submissionTime;
    }

    public void setSubmissiontime(String submissionTime) {
        this.submissionTime = submissionTime;
    }
    public String getLoanid() {
        return loanID;
    }

    public void setLoanid(String loanID) {
        this.loanID = loanID;
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

    public loan_LoanApplication getLoan_loanapplication() {
        return loan_loanapplication;
    }

    public void setLoan_loanapplication(loan_LoanApplication loan_loanapplication) {
        this.loan_loanapplication = loan_loanapplication;
    }

}