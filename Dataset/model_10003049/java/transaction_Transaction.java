





import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private String comment;
    private String destinationAccountNum;
    private float amount;
    private String time;
    private String sourceAccountNum;
    private None type;
    private String transactionID;
    private String description;



    public transaction_Transaction(
        String comment,        String destinationAccountNum,        float amount,        String time,        String sourceAccountNum,        None type,        String transactionID,        String description    ) {
        this.comment = comment;
        this.destinationAccountNum = destinationAccountNum;
        this.amount = amount;
        this.time = time;
        this.sourceAccountNum = sourceAccountNum;
        this.type = type;
        this.transactionID = transactionID;
        this.description = description;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getDestinationaccountnum() {
        return destinationAccountNum;
    }

    public void setDestinationaccountnum(String destinationAccountNum) {
        this.destinationAccountNum = destinationAccountNum;
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
    public String getSourceaccountnum() {
        return sourceAccountNum;
    }

    public void setSourceaccountnum(String sourceAccountNum) {
        this.sourceAccountNum = sourceAccountNum;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getTransactionid() {
        return transactionID;
    }

    public void setTransactionid(String transactionID) {
        this.transactionID = transactionID;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}