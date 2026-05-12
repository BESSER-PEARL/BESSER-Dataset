





import java.util.List;
import java.util.ArrayList;

public class ATMTransactions  {

    private int postBalance;
    private String type;
    private String date;
    private int amount;
    private int transactionid;





    private Account account;


    public ATMTransactions(
        int postBalance,        String type,        String date,        int amount,        int transactionid    ) {
        this.postBalance = postBalance;
        this.type = type;
        this.date = date;
        this.amount = amount;
        this.transactionid = transactionid;
    }


    public int getPostbalance() {
        return postBalance;
    }

    public void setPostbalance(int postBalance) {
        this.postBalance = postBalance;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public int getTransactionid() {
        return transactionid;
    }

    public void setTransactionid(int transactionid) {
        this.transactionid = transactionid;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}