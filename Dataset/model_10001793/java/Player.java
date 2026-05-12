





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private None CardsInHand;
    private boolean isSoft;



    public Player(
        None CardsInHand,        boolean isSoft    ) {
        this.CardsInHand = CardsInHand;
        this.isSoft = isSoft;
    }


    public None getCardsinhand() {
        return CardsInHand;
    }

    public void setCardsinhand(None CardsInHand) {
        this.CardsInHand = CardsInHand;
    }
    public boolean getIssoft() {
        return isSoft;
    }

    public void setIssoft(boolean isSoft) {
        this.isSoft = isSoft;
    }


}