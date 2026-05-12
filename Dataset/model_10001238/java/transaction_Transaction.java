





import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private String destinationAccountNum;
    private None type;
    private String description;
    private String time;
    private String transactionID;
    private float amount;
    private String sourceAccountNum;
    private String comment;





    private account_Account account_account;


    public transaction_Transaction(
        String destinationAccountNum,        None type,        String description,        String time,        String transactionID,        float amount,        String sourceAccountNum,        String comment    ) {
        this.destinationAccountNum = destinationAccountNum;
        this.type = type;
        this.description = description;
        this.time = time;
        this.transactionID = transactionID;
        this.amount = amount;
        this.sourceAccountNum = sourceAccountNum;
        this.comment = comment;
    }


    public String getDestinationaccountnum() {
        return destinationAccountNum;
    }

    public void setDestinationaccountnum(String destinationAccountNum) {
        this.destinationAccountNum = destinationAccountNum;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getTransactionid() {
        return transactionID;
    }

    public void setTransactionid(String transactionID) {
        this.transactionID = transactionID;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public String getSourceaccountnum() {
        return sourceAccountNum;
    }

    public void setSourceaccountnum(String sourceAccountNum) {
        this.sourceAccountNum = sourceAccountNum;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public account_Account getAccount_account() {
        return account_account;
    }

    public void setAccount_account(account_Account account_account) {
        this.account_account = account_account;
    }

}