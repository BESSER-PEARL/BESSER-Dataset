





import java.util.List;
import java.util.ArrayList;

public class Loan_Account  {

    private String Type;
    private int Acc_No;
    private String HolderName;
    private int Loan_No;



    public Loan_Account(
        String Type,        int Acc_No,        String HolderName,        int Loan_No    ) {
        this.Type = Type;
        this.Acc_No = Acc_No;
        this.HolderName = HolderName;
        this.Loan_No = Loan_No;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public int getAcc_no() {
        return Acc_No;
    }

    public void setAcc_no(int Acc_No) {
        this.Acc_No = Acc_No;
    }
    public String getHoldername() {
        return HolderName;
    }

    public void setHoldername(String HolderName) {
        this.HolderName = HolderName;
    }
    public int getLoan_no() {
        return Loan_No;
    }

    public void setLoan_no(int Loan_No) {
        this.Loan_No = Loan_No;
    }


}