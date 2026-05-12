





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private String transactionDate;
    private String transactionAmount;
    private String transactionType;
    private None holder;





    private List<Account> accounts;


    public Transaction(
        String transactionDate,        String transactionAmount,        String transactionType,        None holder    ) {
        this.transactionDate = transactionDate;
        this.transactionAmount = transactionAmount;
        this.transactionType = transactionType;
        this.holder = holder;
        this.accounts = new ArrayList<>();
    }

    public Transaction(
        String transactionDate,        String transactionAmount,        String transactionType,        None holder        ArrayList<Account> accounts    ) {
        this.transactionDate = transactionDate;
        this.transactionAmount = transactionAmount;
        this.transactionType = transactionType;
        this.holder = holder;
        this.accounts = accounts;
    }

    public String getTransactiondate() {
        return transactionDate;
    }

    public void setTransactiondate(String transactionDate) {
        this.transactionDate = transactionDate;
    }
    public String getTransactionamount() {
        return transactionAmount;
    }

    public void setTransactionamount(String transactionAmount) {
        this.transactionAmount = transactionAmount;
    }
    public String getTransactiontype() {
        return transactionType;
    }

    public void setTransactiontype(String transactionType) {
        this.transactionType = transactionType;
    }
    public None getHolder() {
        return holder;
    }

    public void setHolder(None holder) {
        this.holder = holder;
    }

    public List<Account> getAccounts() {
        return accounts;
    }

    public void addAccount(Account account) {
        this.accounts.add(account);
    }

}