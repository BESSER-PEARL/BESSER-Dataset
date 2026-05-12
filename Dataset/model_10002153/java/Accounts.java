





import java.util.List;
import java.util.ArrayList;

public class Accounts  {

    private int AccountNo;
    private String branchCode;





    private Bank bank;


    public Accounts(
        int AccountNo,        String branchCode    ) {
        this.AccountNo = AccountNo;
        this.branchCode = branchCode;
    }


    public int getAccountno() {
        return AccountNo;
    }

    public void setAccountno(int AccountNo) {
        this.AccountNo = AccountNo;
    }
    public String getBranchcode() {
        return branchCode;
    }

    public void setBranchcode(String branchCode) {
        this.branchCode = branchCode;
    }

    public Bank getBank() {
        return bank;
    }

    public void setBank(Bank bank) {
        this.bank = bank;
    }

}