





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_ForkedToken extends Token {

    private String remainingOffersCount;





    private activitydiagram_Token activitydiagram_token;


    public activitydiagram_ForkedToken(
        String remainingOffersCount    ) {
        super(
        );
        this.remainingOffersCount = remainingOffersCount;
    }


    public String getRemainingofferscount() {
        return remainingOffersCount;
    }

    public void setRemainingofferscount(String remainingOffersCount) {
        this.remainingOffersCount = remainingOffersCount;
    }

    public activitydiagram_Token getActivitydiagram_token() {
        return activitydiagram_token;
    }

    public void setActivitydiagram_token(activitydiagram_Token activitydiagram_token) {
        this.activitydiagram_token = activitydiagram_token;
    }

}