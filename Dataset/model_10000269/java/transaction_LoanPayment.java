





import java.util.List;
import java.util.ArrayList;

public class transaction_LoanPayment  {

    private float principal;
    private float interest;
    private String loanID;



    public transaction_LoanPayment(
        float principal,        float interest,        String loanID    ) {
        this.principal = principal;
        this.interest = interest;
        this.loanID = loanID;
    }


    public float getPrincipal() {
        return principal;
    }

    public void setPrincipal(float principal) {
        this.principal = principal;
    }
    public float getInterest() {
        return interest;
    }

    public void setInterest(float interest) {
        this.interest = interest;
    }
    public String getLoanid() {
        return loanID;
    }

    public void setLoanid(String loanID) {
        this.loanID = loanID;
    }


}