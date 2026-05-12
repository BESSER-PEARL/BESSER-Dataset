





import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private String transactionID;
    private String description;
    private String time;
    private String destinationAccountNum;
    private String comment;
    private float amount;
    private String sourceAccountNum;
    private None type;



    public transaction_Transaction(
        String transactionID,        String description,        String time,        String destinationAccountNum,        String comment,        float amount,        String sourceAccountNum,        None type    ) {
        this.transactionID = transactionID;
        this.description = description;
        this.time = time;
        this.destinationAccountNum = destinationAccountNum;
        this.comment = comment;
        this.amount = amount;
        this.sourceAccountNum = sourceAccountNum;
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
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getDestinationaccountnum() {
        return destinationAccountNum;
    }

    public void setDestinationaccountnum(String destinationAccountNum) {
        this.destinationAccountNum = destinationAccountNum;
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
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }


}