





import java.util.List;
import java.util.ArrayList;

public class ATM_Transactions  {

    private String date;
    private String type;
    private String transation_ID;
    private String post_balance;
    private String amount;





    private Account account;


    public ATM_Transactions(
        String date,        String type,        String transation_ID,        String post_balance,        String amount    ) {
        this.date = date;
        this.type = type;
        this.transation_ID = transation_ID;
        this.post_balance = post_balance;
        this.amount = amount;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTransation_id() {
        return transation_ID;
    }

    public void setTransation_id(String transation_ID) {
        this.transation_ID = transation_ID;
    }
    public String getPost_balance() {
        return post_balance;
    }

    public void setPost_balance(String post_balance) {
        this.post_balance = post_balance;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}