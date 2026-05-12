





import java.util.List;
import java.util.ArrayList;

public class loan_LoanApplicationFile  {

    private String applicationID;
    private String fileID;





    private loan_LoanApplication loan_loanapplication;


    public loan_LoanApplicationFile(
        String applicationID,        String fileID    ) {
        this.applicationID = applicationID;
        this.fileID = fileID;
    }


    public String getApplicationid() {
        return applicationID;
    }

    public void setApplicationid(String applicationID) {
        this.applicationID = applicationID;
    }
    public String getFileid() {
        return fileID;
    }

    public void setFileid(String fileID) {
        this.fileID = fileID;
    }

    public loan_LoanApplication getLoan_loanapplication() {
        return loan_loanapplication;
    }

    public void setLoan_loanapplication(loan_LoanApplication loan_loanapplication) {
        this.loan_loanapplication = loan_loanapplication;
    }

}