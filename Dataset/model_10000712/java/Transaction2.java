





import java.util.List;
import java.util.ArrayList;

public class Transaction2  {

    private String description;
    private String transactionID;
    private String comment;
    private String time;
    private String destinationAccountNum;
    private float amount;
    private String sourceAccountNum;
    private None type;



    public Transaction2(
        String description,        String transactionID,        String comment,        String time,        String destinationAccountNum,        float amount,        String sourceAccountNum,        None type    ) {
        this.description = description;
        this.transactionID = transactionID;
        this.comment = comment;
        this.time = time;
        this.destinationAccountNum = destinationAccountNum;
        this.amount = amount;
        this.sourceAccountNum = sourceAccountNum;
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
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
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