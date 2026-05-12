





import java.util.List;
import java.util.ArrayList;

public class ATM__Transactions  {

    private int Remaining_balance;
    private int Transaction_amount;
    private String Type;
    private String Transaction_id;





    private Account account;


    public ATM__Transactions(
        int Remaining_balance,        int Transaction_amount,        String Type,        String Transaction_id    ) {
        this.Remaining_balance = Remaining_balance;
        this.Transaction_amount = Transaction_amount;
        this.Type = Type;
        this.Transaction_id = Transaction_id;
    }


    public int getRemaining_balance() {
        return Remaining_balance;
    }

    public void setRemaining_balance(int Remaining_balance) {
        this.Remaining_balance = Remaining_balance;
    }
    public int getTransaction_amount() {
        return Transaction_amount;
    }

    public void setTransaction_amount(int Transaction_amount) {
        this.Transaction_amount = Transaction_amount;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getTransaction_id() {
        return Transaction_id;
    }

    public void setTransaction_id(String Transaction_id) {
        this.Transaction_id = Transaction_id;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}