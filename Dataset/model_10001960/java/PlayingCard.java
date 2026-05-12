





import java.util.List;
import java.util.ArrayList;

public class PlayingCard  {

    private boolean faceUp;
    private boolean jokerCard;
    private boolean standardCard;



    public PlayingCard(
        boolean faceUp,        boolean jokerCard,        boolean standardCard    ) {
        this.faceUp = faceUp;
        this.jokerCard = jokerCard;
        this.standardCard = standardCard;
    }


    public boolean getFaceup() {
        return faceUp;
    }

    public void setFaceup(boolean faceUp) {
        this.faceUp = faceUp;
    }
    public boolean getJokercard() {
        return jokerCard;
    }

    public void setJokercard(boolean jokerCard) {
        this.jokerCard = jokerCard;
    }
    public boolean getStandardcard() {
        return standardCard;
    }

    public void setStandardcard(boolean standardCard) {
        this.standardCard = standardCard;
    }


}