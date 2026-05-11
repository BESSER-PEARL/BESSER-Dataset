





import java.util.List;
import java.util.ArrayList;

public class iot2_ForkedToken extends Token {

    private String remainingOffersCount;



    public iot2_ForkedToken(
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


}