





import java.util.List;
import java.util.ArrayList;

public class Transaction1  {

    private String sourceAccountNum;
    private String description;
    private String comment;
    private float amount;
    private None type;
    private String time;
    private String destinationAccountNum;
    private String transactionID;





    private Account1 account1;


    public Transaction1(
        String sourceAccountNum,        String description,        String comment,        float amount,        None type,        String time,        String destinationAccountNum,        String transactionID    ) {
        this.sourceAccountNum = sourceAccountNum;
        this.description = description;
        this.comment = comment;
        this.amount = amount;
        this.type = type;
        this.time = time;
        this.destinationAccountNum = destinationAccountNum;
        this.transactionID = transactionID;
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
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
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
    public String getTransactionid() {
        return transactionID;
    }

    public void setTransactionid(String transactionID) {
        this.transactionID = transactionID;
    }

    public Account1 getAccount1() {
        return account1;
    }

    public void setAccount1(Account1 account1) {
        this.account1 = account1;
    }

}