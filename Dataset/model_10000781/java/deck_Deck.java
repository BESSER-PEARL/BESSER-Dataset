





import java.util.List;
import java.util.ArrayList;

public class deck_Deck  {

    private int inputDestinationRow;
    private int stepCounter;
    private int foundationIndex;
    private int removeItemFromArrayIndex;
    private int score;





    private card_Deck card_deck;


    public deck_Deck(
        int inputDestinationRow,        int stepCounter,        int foundationIndex,        int removeItemFromArrayIndex,        int score    ) {
        this.inputDestinationRow = inputDestinationRow;
        this.stepCounter = stepCounter;
        this.foundationIndex = foundationIndex;
        this.removeItemFromArrayIndex = removeItemFromArrayIndex;
        this.score = score;
    }


    public int getInputdestinationrow() {
        return inputDestinationRow;
    }

    public void setInputdestinationrow(int inputDestinationRow) {
        this.inputDestinationRow = inputDestinationRow;
    }
    public int getStepcounter() {
        return stepCounter;
    }

    public void setStepcounter(int stepCounter) {
        this.stepCounter = stepCounter;
    }
    public int getFoundationindex() {
        return foundationIndex;
    }

    public void setFoundationindex(int foundationIndex) {
        this.foundationIndex = foundationIndex;
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

    public card_Deck getCard_deck() {
        return card_deck;
    }

    public void setCard_deck(card_Deck card_deck) {
        this.card_deck = card_deck;
    }

}