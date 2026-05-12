





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private String transactionID;
    private String sourceAccountNum;
    private String comment;
    private String description;
    private float amount;
    private String time;
    private None type;
    private String destinationAccountNum;



    public Transaction(
        String transactionID,        String sourceAccountNum,        String comment,        String description,        float amount,        String time,        None type,        String destinationAccountNum    ) {
        this.transactionID = transactionID;
        this.sourceAccountNum = sourceAccountNum;
        this.comment = comment;
        this.description = description;
        this.amount = amount;
        this.time = time;
        this.type = type;
        this.destinationAccountNum = destinationAccountNum;
    }


    public String getTransactionid() {
        return transactionID;
    }

    public void setTransactionid(String transactionID) {
        this.transactionID = transactionID;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
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


}