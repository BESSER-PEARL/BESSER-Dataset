





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private boolean isSoft;
    private None CardsInHand;



    public Player(
        boolean isSoft,        None CardsInHand    ) {
        this.isSoft = isSoft;
        this.CardsInHand = CardsInHand;
    }


    public boolean getIssoft() {
        return isSoft;
    }

    public void setIssoft(boolean isSoft) {
        this.isSoft = isSoft;
    }
    public None getCardsinhand() {
        return CardsInHand;
    }

    public void setCardsinhand(None CardsInHand) {
        this.CardsInHand = CardsInHand;
    }


}