





import java.util.List;
import java.util.ArrayList;

public class DealDeck  {

    private String EASY_THROUGH_LIMIT;
    private String deckThroughLimit;
    private String HARD_THROUGH_LIMIT;
    private String discardPile;
    private String DRAW_THREE_THROUGH_LIMIT;
    private String numTimesThroughDeck;
    private String drawCount;
    private String DRAW_ONE_THROUGH_LIMIT;
    private String difficulty;
    private String MEDIUM_THROUGH_LIMIT;
    private boolean redealable;



    public DealDeck(
        String EASY_THROUGH_LIMIT,        String deckThroughLimit,        String HARD_THROUGH_LIMIT,        String discardPile,        String DRAW_THREE_THROUGH_LIMIT,        String numTimesThroughDeck,        String drawCount,        String DRAW_ONE_THROUGH_LIMIT,        String difficulty,        String MEDIUM_THROUGH_LIMIT,        boolean redealable    ) {
        this.EASY_THROUGH_LIMIT = EASY_THROUGH_LIMIT;
        this.deckThroughLimit = deckThroughLimit;
        this.HARD_THROUGH_LIMIT = HARD_THROUGH_LIMIT;
        this.discardPile = discardPile;
        this.DRAW_THREE_THROUGH_LIMIT = DRAW_THREE_THROUGH_LIMIT;
        this.numTimesThroughDeck = numTimesThroughDeck;
        this.drawCount = drawCount;
        this.DRAW_ONE_THROUGH_LIMIT = DRAW_ONE_THROUGH_LIMIT;
        this.difficulty = difficulty;
        this.MEDIUM_THROUGH_LIMIT = MEDIUM_THROUGH_LIMIT;
        this.redealable = redealable;
    }


    public String getEasy_through_limit() {
        return EASY_THROUGH_LIMIT;
    }

    public void setEasy_through_limit(String EASY_THROUGH_LIMIT) {
        this.EASY_THROUGH_LIMIT = EASY_THROUGH_LIMIT;
    }
    public String getDeckthroughlimit() {
        return deckThroughLimit;
    }

    public void setDeckthroughlimit(String deckThroughLimit) {
        this.deckThroughLimit = deckThroughLimit;
    }
    public String getHard_through_limit() {
        return HARD_THROUGH_LIMIT;
    }

    public void setHard_through_limit(String HARD_THROUGH_LIMIT) {
        this.HARD_THROUGH_LIMIT = HARD_THROUGH_LIMIT;
    }
    public String getDiscardpile() {
        return discardPile;
    }

    public void setDiscardpile(String discardPile) {
        this.discardPile = discardPile;
    }
    public String getDraw_three_through_limit() {
        return DRAW_THREE_THROUGH_LIMIT;
    }

    public void setDraw_three_through_limit(String DRAW_THREE_THROUGH_LIMIT) {
        this.DRAW_THREE_THROUGH_LIMIT = DRAW_THREE_THROUGH_LIMIT;
    }
    public String getNumtimesthroughdeck() {
        return numTimesThroughDeck;
    }

    public void setNumtimesthroughdeck(String numTimesThroughDeck) {
        this.numTimesThroughDeck = numTimesThroughDeck;
    }
    public String getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(String drawCount) {
        this.drawCount = drawCount;
    }
    public String getDraw_one_through_limit() {
        return DRAW_ONE_THROUGH_LIMIT;
    }

    public void setDraw_one_through_limit(String DRAW_ONE_THROUGH_LIMIT) {
        this.DRAW_ONE_THROUGH_LIMIT = DRAW_ONE_THROUGH_LIMIT;
    }
    public String getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(String difficulty) {
        this.difficulty = difficulty;
    }
    public String getMedium_through_limit() {
        return MEDIUM_THROUGH_LIMIT;
    }

    public void setMedium_through_limit(String MEDIUM_THROUGH_LIMIT) {
        this.MEDIUM_THROUGH_LIMIT = MEDIUM_THROUGH_LIMIT;
    }
    public boolean getRedealable() {
        return redealable;
    }

    public void setRedealable(boolean redealable) {
        this.redealable = redealable;
    }


}