





import java.util.List;
import java.util.ArrayList;

public class transaction_LoanPayment  {

    private float principal;
    private String loanID;
    private float interest;



    public transaction_LoanPayment(
        float principal,        String loanID,        float interest    ) {
        this.principal = principal;
        this.loanID = loanID;
        this.interest = interest;
    }


    public float getPrincipal() {
        return principal;
    }

    public void setPrincipal(float principal) {
        this.principal = principal;
    }
    public String getLoanid() {
        return loanID;
    }

    public void setLoanid(String loanID) {
        this.loanID = loanID;
    }
    public float getInterest() {
        return interest;
    }

    public void setInterest(float interest) {
        this.interest = interest;
    }


}