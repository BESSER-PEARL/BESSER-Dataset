





import java.util.List;
import java.util.ArrayList;

public class SavingAccount  {

    private int balance;
    private int accountNo;





    private CurrentAccount currentaccount;


    public SavingAccount(
        int balance,        int accountNo    ) {
        this.balance = balance;
        this.accountNo = accountNo;
    }


    public int getBalance() {
        return balance;
    }

    public void setBalance(int balance) {
        this.balance = balance;
    }
    public int getAccountno() {
        return accountNo;
    }

    public void setAccountno(int accountNo) {
        this.accountNo = accountNo;
    }

    public CurrentAccount getCurrentaccount() {
        return currentaccount;
    }

    public void setCurrentaccount(CurrentAccount currentaccount) {
        this.currentaccount = currentaccount;
    }

}