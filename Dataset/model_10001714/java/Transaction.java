





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private int accountNo;
    private int transactionId;
    private String amount;
    private String description;
    private None transactionType;
    private String transactionDate;



    public Transaction(
        int accountNo,        int transactionId,        String amount,        String description,        None transactionType,        String transactionDate    ) {
        this.accountNo = accountNo;
        this.transactionId = transactionId;
        this.amount = amount;
        this.description = description;
        this.transactionType = transactionType;
        this.transactionDate = transactionDate;
    }


    public int getAccountno() {
        return accountNo;
    }

    public void setAccountno(int accountNo) {
        this.accountNo = accountNo;
    }
    public int getTransactionid() {
        return transactionId;
    }

    public void setTransactionid(int transactionId) {
        this.transactionId = transactionId;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public None getTransactiontype() {
        return transactionType;
    }

    public void setTransactiontype(None transactionType) {
        this.transactionType = transactionType;
    }
    public String getTransactiondate() {
        return transactionDate;
    }

    public void setTransactiondate(String transactionDate) {
        this.transactionDate = transactionDate;
    }


}