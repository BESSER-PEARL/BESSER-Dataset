





import java.util.List;
import java.util.ArrayList;

public class JokerCard  {

    private boolean jokerCard;
    private boolean red;



    public JokerCard(
        boolean jokerCard,        boolean red    ) {
        this.jokerCard = jokerCard;
        this.red = red;
    }


    public boolean getJokercard() {
        return jokerCard;
    }

    public void setJokercard(boolean jokerCard) {
        this.jokerCard = jokerCard;
    }
    public boolean getRed() {
        return red;
    }

    public void setRed(boolean red) {
        this.red = red;
    }


}