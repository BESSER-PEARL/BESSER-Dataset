





import java.util.List;
import java.util.ArrayList;

public class Transaction3  {

    private String time;
    private String comment;
    private String sourceAccountNum;
    private float amount;
    private None type;
    private String description;
    private String transactionID;
    private String destinationAccountNum;





    private Account2 account2;


    public Transaction3(
        String time,        String comment,        String sourceAccountNum,        float amount,        None type,        String description,        String transactionID,        String destinationAccountNum    ) {
        this.time = time;
        this.comment = comment;
        this.sourceAccountNum = sourceAccountNum;
        this.amount = amount;
        this.type = type;
        this.description = description;
        this.transactionID = transactionID;
        this.destinationAccountNum = destinationAccountNum;
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
    public String getSourceaccountnum() {
        return sourceAccountNum;
    }

    public void setSourceaccountnum(String sourceAccountNum) {
        this.sourceAccountNum = sourceAccountNum;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
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
    public String getTransactionid() {
        return transactionID;
    }

    public void setTransactionid(String transactionID) {
        this.transactionID = transactionID;
    }
    public String getDestinationaccountnum() {
        return destinationAccountNum;
    }

    public void setDestinationaccountnum(String destinationAccountNum) {
        this.destinationAccountNum = destinationAccountNum;
    }

    public Account2 getAccount2() {
        return account2;
    }

    public void setAccount2(Account2 account2) {
        this.account2 = account2;
    }

}