





import java.util.List;
import java.util.ArrayList;

public class Loan  {

    private String emp_name;
    private String loan_type;
    private int emp_id;
    private String amount;
    private int loan_interst;
    private String loan_purpose;



    public Loan(
        String emp_name,        String loan_type,        int emp_id,        String amount,        int loan_interst,        String loan_purpose    ) {
        this.emp_name = emp_name;
        this.loan_type = loan_type;
        this.emp_id = emp_id;
        this.amount = amount;
        this.loan_interst = loan_interst;
        this.loan_purpose = loan_purpose;
    }


    public String getEmp_name() {
        return emp_name;
    }

    public void setEmp_name(String emp_name) {
        this.emp_name = emp_name;
    }
    public String getLoan_type() {
        return loan_type;
    }

    public void setLoan_type(String loan_type) {
        this.loan_type = loan_type;
    }
    public int getEmp_id() {
        return emp_id;
    }

    public void setEmp_id(int emp_id) {
        this.emp_id = emp_id;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public int getLoan_interst() {
        return loan_interst;
    }

    public void setLoan_interst(int loan_interst) {
        this.loan_interst = loan_interst;
    }
    public String getLoan_purpose() {
        return loan_purpose;
    }

    public void setLoan_purpose(String loan_purpose) {
        this.loan_purpose = loan_purpose;
    }


}