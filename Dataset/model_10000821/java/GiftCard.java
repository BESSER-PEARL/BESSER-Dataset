





import java.util.List;
import java.util.ArrayList;

public class GiftCard  {

    private None cardType;
    private boolean isPresent;



    public GiftCard(
        None cardType,        boolean isPresent    ) {
        this.cardType = cardType;
        this.isPresent = isPresent;
    }


    public None getCardtype() {
        return cardType;
    }

    public void setCardtype(None cardType) {
        this.cardType = cardType;
    }
    public boolean getIspresent() {
        return isPresent;
    }

    public void setIspresent(boolean isPresent) {
        this.isPresent = isPresent;
    }


}