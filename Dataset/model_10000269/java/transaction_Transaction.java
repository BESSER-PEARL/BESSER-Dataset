





import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private String transactionID;
    private None type;
    private String destinationAccountNum;
    private String description;
    private String time;
    private String comment;
    private float amount;
    private String sourceAccountNum;





    private account_Account account_account;


    public transaction_Transaction(
        String transactionID,        None type,        String destinationAccountNum,        String description,        String time,        String comment,        float amount,        String sourceAccountNum    ) {
        this.transactionID = transactionID;
        this.type = type;
        this.destinationAccountNum = destinationAccountNum;
        this.description = description;
        this.time = time;
        this.comment = comment;
        this.amount = amount;
        this.sourceAccountNum = sourceAccountNum;
    }


    public String getTransactionid() {
        return transactionID;
    }

    public void setTransactionid(String transactionID) {
        this.transactionID = transactionID;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getDestinationaccountnum() {
        return destinationAccountNum;
    }

    public void setDestinationaccountnum(String destinationAccountNum) {
        this.destinationAccountNum = destinationAccountNum;
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
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
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

    public account_Account getAccount_account() {
        return account_account;
    }

    public void setAccount_account(account_Account account_account) {
        this.account_account = account_account;
    }

}