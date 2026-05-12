





import java.util.List;
import java.util.ArrayList;

public class ATM__Transactions  {

    private String Transaction_id;
    private String Type;
    private String Date;
    private String Amount;
    private String Post_balance;





    private Account account;


    public ATM__Transactions(
        String Transaction_id,        String Type,        String Date,        String Amount,        String Post_balance    ) {
        this.Transaction_id = Transaction_id;
        this.Type = Type;
        this.Date = Date;
        this.Amount = Amount;
        this.Post_balance = Post_balance;
    }


    public String getTransaction_id() {
        return Transaction_id;
    }

    public void setTransaction_id(String Transaction_id) {
        this.Transaction_id = Transaction_id;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }
    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }
    public String getPost_balance() {
        return Post_balance;
    }

    public void setPost_balance(String Post_balance) {
        this.Post_balance = Post_balance;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}