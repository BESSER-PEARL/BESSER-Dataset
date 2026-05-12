





import java.util.List;
import java.util.ArrayList;

public class deck_Deck  {

    private int score;
    private int stepCounter;
    private int inputDestinationRow;
    private int removeItemFromArrayIndex;
    private int foundationIndex;





    private card_Pack card_pack;


    public deck_Deck(
        int score,        int stepCounter,        int inputDestinationRow,        int removeItemFromArrayIndex,        int foundationIndex    ) {
        this.score = score;
        this.stepCounter = stepCounter;
        this.inputDestinationRow = inputDestinationRow;
        this.removeItemFromArrayIndex = removeItemFromArrayIndex;
        this.foundationIndex = foundationIndex;
    }


    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    public int getStepcounter() {
        return stepCounter;
    }

    public void setStepcounter(int stepCounter) {
        this.stepCounter = stepCounter;
    }
    public int getInputdestinationrow() {
        return inputDestinationRow;
    }

    public void setInputdestinationrow(int inputDestinationRow) {
        this.inputDestinationRow = inputDestinationRow;
    }
    public int getRemoveitemfromarrayindex() {
        return removeItemFromArrayIndex;
    }

    public void setRemoveitemfromarrayindex(int removeItemFromArrayIndex) {
        this.removeItemFromArrayIndex = removeItemFromArrayIndex;
    }
    public int getFoundationindex() {
        return foundationIndex;
    }

    public void setFoundationindex(int foundationIndex) {
        this.foundationIndex = foundationIndex;
    }

    public card_Pack getCard_pack() {
        return card_pack;
    }

    public void setCard_pack(card_Pack card_pack) {
        this.card_pack = card_pack;
    }

}