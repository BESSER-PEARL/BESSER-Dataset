





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_ForkedToken extends Token {

    private int remainingOffersCount;





    private activitydiagram_Token activitydiagram_token;


    public activitydiagram_ForkedToken(
        int remainingOffersCount    ) {
        super(
        );
        this.remainingOffersCount = remainingOffersCount;
    }


    public int getRemainingofferscount() {
        return remainingOffersCount;
    }

    public void setRemainingofferscount(int remainingOffersCount) {
        this.remainingOffersCount = remainingOffersCount;
    }

    public activitydiagram_Token getActivitydiagram_token() {
        return activitydiagram_token;
    }

    public void setActivitydiagram_token(activitydiagram_Token activitydiagram_token) {
        this.activitydiagram_token = activitydiagram_token;
    }

}