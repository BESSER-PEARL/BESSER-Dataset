





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private String transactionDate;
    private String transactionType;
    private String transactionAmount;
    private None holder;





    private List<Account> accounts;


    public Transaction(
        String transactionDate,        String transactionType,        String transactionAmount,        None holder    ) {
        this.transactionDate = transactionDate;
        this.transactionType = transactionType;
        this.transactionAmount = transactionAmount;
        this.holder = holder;
        this.accounts = new ArrayList<>();
    }

    public Transaction(
        String transactionDate,        String transactionType,        String transactionAmount,        None holder        ArrayList<Account> accounts    ) {
        this.transactionDate = transactionDate;
        this.transactionType = transactionType;
        this.transactionAmount = transactionAmount;
        this.holder = holder;
        this.accounts = accounts;
    }

    public String getTransactiondate() {
        return transactionDate;
    }

    public void setTransactiondate(String transactionDate) {
        this.transactionDate = transactionDate;
    }
    public String getTransactiontype() {
        return transactionType;
    }

    public void setTransactiontype(String transactionType) {
        this.transactionType = transactionType;
    }
    public String getTransactionamount() {
        return transactionAmount;
    }

    public void setTransactionamount(String transactionAmount) {
        this.transactionAmount = transactionAmount;
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