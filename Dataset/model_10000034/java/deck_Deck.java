





import java.util.List;
import java.util.ArrayList;

public class deck_Deck  {

    private int stepCounter;
    private int removeItemFromArrayIndex;
    private int score;
    private int foundationIndex;
    private int inputDestinationRow;





    private card_Pack card_pack;


    public deck_Deck(
        int stepCounter,        int removeItemFromArrayIndex,        int score,        int foundationIndex,        int inputDestinationRow    ) {
        this.stepCounter = stepCounter;
        this.removeItemFromArrayIndex = removeItemFromArrayIndex;
        this.score = score;
        this.foundationIndex = foundationIndex;
        this.inputDestinationRow = inputDestinationRow;
    }


    public int getStepcounter() {
        return stepCounter;
    }

    public void setStepcounter(int stepCounter) {
        this.stepCounter = stepCounter;
    }
    public int getRemoveitemfromarrayindex() {
        return removeItemFromArrayIndex;
    }

    public void setRemoveitemfromarrayindex(int removeItemFromArrayIndex) {
        this.removeItemFromArrayIndex = removeItemFromArrayIndex;
    }
    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    public int getFoundationindex() {
        return foundationIndex;
    }

    public void setFoundationindex(int foundationIndex) {
        this.foundationIndex = foundationIndex;
    }
    public int getInputdestinationrow() {
        return inputDestinationRow;
    }

    public void setInputdestinationrow(int inputDestinationRow) {
        this.inputDestinationRow = inputDestinationRow;
    }

    public card_Pack getCard_pack() {
        return card_pack;
    }

    public void setCard_pack(card_Pack card_pack) {
        this.card_pack = card_pack;
    }

}