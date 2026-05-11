





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Offer  {






    private activitydiagram_ActivityEdge activitydiagram_activityedge;




    private List<activitydiagram_Token> activitydiagram_tokens;


    public activitydiagram_Offer(
    ) {
        this.activitydiagram_tokens = new ArrayList<>();
    }

    public activitydiagram_Offer(
        ArrayList<activitydiagram_Token> activitydiagram_tokens    ) {
        this.activitydiagram_tokens = activitydiagram_tokens;
    }


    public activitydiagram_ActivityEdge getActivitydiagram_activityedge() {
        return activitydiagram_activityedge;
    }

    public void setActivitydiagram_activityedge(activitydiagram_ActivityEdge activitydiagram_activityedge) {
        this.activitydiagram_activityedge = activitydiagram_activityedge;
    }
    public List<activitydiagram_Token> getActivitydiagram_tokens() {
        return activitydiagram_tokens;
    }

    public void addActivitydiagram_token(Activitydiagram_token activitydiagram_token) {
        this.activitydiagram_tokens.add(activitydiagram_token);
    }

}