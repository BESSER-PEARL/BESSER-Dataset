





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_ForkedToken extends Token {

    private int remainingOffersCount;



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


}