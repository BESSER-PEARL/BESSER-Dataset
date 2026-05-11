





import java.util.List;
import java.util.ArrayList;

public class behavior_Session  {

    private String id;
    private String startTime;
    private String transactionType;
    private String endTime;





    private behavior_SessionRepository behavior_sessionrepository;


    public behavior_Session(
        String id,        String startTime,        String transactionType,        String endTime    ) {
        this.id = id;
        this.startTime = startTime;
        this.transactionType = transactionType;
        this.endTime = endTime;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public String getTransactiontype() {
        return transactionType;
    }

    public void setTransactiontype(String transactionType) {
        this.transactionType = transactionType;
    }
    public String getEndtime() {
        return endTime;
    }

    public void setEndtime(String endTime) {
        this.endTime = endTime;
    }

    public behavior_SessionRepository getBehavior_sessionrepository() {
        return behavior_sessionrepository;
    }

    public void setBehavior_sessionrepository(behavior_SessionRepository behavior_sessionrepository) {
        this.behavior_sessionrepository = behavior_sessionrepository;
    }

}