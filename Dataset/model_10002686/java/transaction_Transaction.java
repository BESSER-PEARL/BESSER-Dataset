





import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private String transactionID;
    private String comment;
    private None type;
    private String destinationAccountNum;
    private String sourceAccountNum;
    private String description;
    private float amount;
    private String time;



    public transaction_Transaction(
        String transactionID,        String comment,        None type,        String destinationAccountNum,        String sourceAccountNum,        String description,        float amount,        String time    ) {
        this.transactionID = transactionID;
        this.comment = comment;
        this.type = type;
        this.destinationAccountNum = destinationAccountNum;
        this.sourceAccountNum = sourceAccountNum;
        this.description = description;
        this.amount = amount;
        this.time = time;
    }


    public String getTransactionid() {
        return transactionID;
    }

    public void setTransactionid(String transactionID) {
        this.transactionID = transactionID;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
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
    public String getSourceaccountnum() {
        return sourceAccountNum;
    }

    public void setSourceaccountnum(String sourceAccountNum) {
        this.sourceAccountNum = sourceAccountNum;
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


}