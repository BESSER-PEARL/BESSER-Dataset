





import java.util.List;
import java.util.ArrayList;

public class QuotaItem  {

    private String id;
    private String sueprClassId;
    private int amount;
    private String quotaItemName;
    private None type;
    private String createdOn;
    private String comment;





    private Quota quota;


    public QuotaItem(
        String id,        String sueprClassId,        int amount,        String quotaItemName,        None type,        String createdOn,        String comment    ) {
        this.id = id;
        this.sueprClassId = sueprClassId;
        this.amount = amount;
        this.quotaItemName = quotaItemName;
        this.type = type;
        this.createdOn = createdOn;
        this.comment = comment;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSueprclassid() {
        return sueprClassId;
    }

    public void setSueprclassid(String sueprClassId) {
        this.sueprClassId = sueprClassId;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }
    public String getQuotaitemname() {
        return quotaItemName;
    }

    public void setQuotaitemname(String quotaItemName) {
        this.quotaItemName = quotaItemName;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public String getCreatedon() {
        return createdOn;
    }

    public void setCreatedon(String createdOn) {
        this.createdOn = createdOn;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public Quota getQuota() {
        return quota;
    }

    public void setQuota(Quota quota) {
        this.quota = quota;
    }

}