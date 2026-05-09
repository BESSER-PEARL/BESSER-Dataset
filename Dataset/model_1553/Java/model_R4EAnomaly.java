




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class model_R4EAnomaly extends R4EComment, Topic, R4EReviewComponent {

    private LocalDate dueDate;
    private String fixedByID;
    private String followUpByID;
    private String state;
    private String notAcceptedReason;
    private boolean isImported;
    private String ruleID;
    private String decidedByID;
    private String rank;



    public model_R4EAnomaly(
        LocalDate dueDate,        String fixedByID,        String followUpByID,        String state,        String notAcceptedReason,        boolean isImported,        String ruleID,        String decidedByID,        String rank    ) {
        super(
        );
        this.dueDate = dueDate;
        this.fixedByID = fixedByID;
        this.followUpByID = followUpByID;
        this.state = state;
        this.notAcceptedReason = notAcceptedReason;
        this.isImported = isImported;
        this.ruleID = ruleID;
        this.decidedByID = decidedByID;
        this.rank = rank;
    }


    public LocalDate getDuedate() {
        return dueDate;
    }

    public void setDuedate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }
    public String getFixedbyid() {
        return fixedByID;
    }

    public void setFixedbyid(String fixedByID) {
        this.fixedByID = fixedByID;
    }
    public String getFollowupbyid() {
        return followUpByID;
    }

    public void setFollowupbyid(String followUpByID) {
        this.followUpByID = followUpByID;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getNotacceptedreason() {
        return notAcceptedReason;
    }

    public void setNotacceptedreason(String notAcceptedReason) {
        this.notAcceptedReason = notAcceptedReason;
    }
    public boolean getIsimported() {
        return isImported;
    }

    public void setIsimported(boolean isImported) {
        this.isImported = isImported;
    }
    public String getRuleid() {
        return ruleID;
    }

    public void setRuleid(String ruleID) {
        this.ruleID = ruleID;
    }
    public String getDecidedbyid() {
        return decidedByID;
    }

    public void setDecidedbyid(String decidedByID) {
        this.decidedByID = decidedByID;
    }
    public String getRank() {
        return rank;
    }

    public void setRank(String rank) {
        this.rank = rank;
    }


}