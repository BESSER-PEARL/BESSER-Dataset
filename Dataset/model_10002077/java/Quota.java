





import java.util.List;
import java.util.ArrayList;

public class Quota  {

    private String comment;
    private String id;
    private int current;
    private int max;
    private String quotaName;



    public Quota(
        String comment,        String id,        int current,        int max,        String quotaName    ) {
        this.comment = comment;
        this.id = id;
        this.current = current;
        this.max = max;
        this.quotaName = quotaName;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getCurrent() {
        return current;
    }

    public void setCurrent(int current) {
        this.current = current;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }
    public String getQuotaname() {
        return quotaName;
    }

    public void setQuotaname(String quotaName) {
        this.quotaName = quotaName;
    }


}