





import java.util.List;
import java.util.ArrayList;

public class loan_Loan  {

    private None status;
    private None type;
    private String submissionTime;
    private String loanID;
    private float amount;
    private int term;
    private float interestRate;
    private String userID;





    private loan_LoanApplication loan_loanapplication;


    public loan_Loan(
        None status,        None type,        String submissionTime,        String loanID,        float amount,        int term,        float interestRate,        String userID    ) {
        this.status = status;
        this.type = type;
        this.submissionTime = submissionTime;
        this.loanID = loanID;
        this.amount = amount;
        this.term = term;
        this.interestRate = interestRate;
        this.userID = userID;
    }


    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
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
    public String getLoanid() {
        return loanID;
    }

    public void setLoanid(String loanID) {
        this.loanID = loanID;
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
    public float getInterestrate() {
        return interestRate;
    }

    public void setInterestrate(float interestRate) {
        this.interestRate = interestRate;
    }
    public String getUserid() {
        return userID;
    }

    public void setUserid(String userID) {
        this.userID = userID;
    }

    public loan_LoanApplication getLoan_loanapplication() {
        return loan_loanapplication;
    }

    public void setLoan_loanapplication(loan_LoanApplication loan_loanapplication) {
        this.loan_loanapplication = loan_loanapplication;
    }

}