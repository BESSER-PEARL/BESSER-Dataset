





import java.util.List;
import java.util.ArrayList;

public class Account  {

    private int min_Balance;
    private String date_Of_Opening;
    private int Balance;
    private int Acc_no;





    private Branch branch;


    public Account(
        int min_Balance,        String date_Of_Opening,        int Balance,        int Acc_no    ) {
        this.min_Balance = min_Balance;
        this.date_Of_Opening = date_Of_Opening;
        this.Balance = Balance;
        this.Acc_no = Acc_no;
    }


    public int getMin_balance() {
        return min_Balance;
    }

    public void setMin_balance(int min_Balance) {
        this.min_Balance = min_Balance;
    }
    public String getDate_of_opening() {
        return date_Of_Opening;
    }

    public void setDate_of_opening(String date_Of_Opening) {
        this.date_Of_Opening = date_Of_Opening;
    }
    public int getBalance() {
        return Balance;
    }

    public void setBalance(int Balance) {
        this.Balance = Balance;
    }
    public int getAcc_no() {
        return Acc_no;
    }

    public void setAcc_no(int Acc_no) {
        this.Acc_no = Acc_no;
    }

    public Branch getBranch() {
        return branch;
    }

    public void setBranch(Branch branch) {
        this.branch = branch;
    }

}