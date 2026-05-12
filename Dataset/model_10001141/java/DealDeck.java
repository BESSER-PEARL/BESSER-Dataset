





import java.util.List;
import java.util.ArrayList;

public class DealDeck  {

    private String discardPile;
    private String DRAW_ONE_THROUGH_LIMIT;
    private String DRAW_THREE_THROUGH_LIMIT;
    private boolean redealable;
    private String difficulty;
    private String deckThroughLimit;
    private String EASY_THROUGH_LIMIT;
    private String numTimesThroughDeck;
    private String HARD_THROUGH_LIMIT;
    private String MEDIUM_THROUGH_LIMIT;
    private String drawCount;



    public DealDeck(
        String discardPile,        String DRAW_ONE_THROUGH_LIMIT,        String DRAW_THREE_THROUGH_LIMIT,        boolean redealable,        String difficulty,        String deckThroughLimit,        String EASY_THROUGH_LIMIT,        String numTimesThroughDeck,        String HARD_THROUGH_LIMIT,        String MEDIUM_THROUGH_LIMIT,        String drawCount    ) {
        this.discardPile = discardPile;
        this.DRAW_ONE_THROUGH_LIMIT = DRAW_ONE_THROUGH_LIMIT;
        this.DRAW_THREE_THROUGH_LIMIT = DRAW_THREE_THROUGH_LIMIT;
        this.redealable = redealable;
        this.difficulty = difficulty;
        this.deckThroughLimit = deckThroughLimit;
        this.EASY_THROUGH_LIMIT = EASY_THROUGH_LIMIT;
        this.numTimesThroughDeck = numTimesThroughDeck;
        this.HARD_THROUGH_LIMIT = HARD_THROUGH_LIMIT;
        this.MEDIUM_THROUGH_LIMIT = MEDIUM_THROUGH_LIMIT;
        this.drawCount = drawCount;
    }


    public String getDiscardpile() {
        return discardPile;
    }

    public void setDiscardpile(String discardPile) {
        this.discardPile = discardPile;
    }
    public String getDraw_one_through_limit() {
        return DRAW_ONE_THROUGH_LIMIT;
    }

    public void setDraw_one_through_limit(String DRAW_ONE_THROUGH_LIMIT) {
        this.DRAW_ONE_THROUGH_LIMIT = DRAW_ONE_THROUGH_LIMIT;
    }
    public String getDraw_three_through_limit() {
        return DRAW_THREE_THROUGH_LIMIT;
    }

    public void setDraw_three_through_limit(String DRAW_THREE_THROUGH_LIMIT) {
        this.DRAW_THREE_THROUGH_LIMIT = DRAW_THREE_THROUGH_LIMIT;
    }
    public boolean getRedealable() {
        return redealable;
    }

    public void setRedealable(boolean redealable) {
        this.redealable = redealable;
    }
    public String getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(String difficulty) {
        this.difficulty = difficulty;
    }
    public String getDeckthroughlimit() {
        return deckThroughLimit;
    }

    public void setDeckthroughlimit(String deckThroughLimit) {
        this.deckThroughLimit = deckThroughLimit;
    }
    public String getEasy_through_limit() {
        return EASY_THROUGH_LIMIT;
    }

    public void setEasy_through_limit(String EASY_THROUGH_LIMIT) {
        this.EASY_THROUGH_LIMIT = EASY_THROUGH_LIMIT;
    }
    public String getNumtimesthroughdeck() {
        return numTimesThroughDeck;
    }

    public void setNumtimesthroughdeck(String numTimesThroughDeck) {
        this.numTimesThroughDeck = numTimesThroughDeck;
    }
    public String getHard_through_limit() {
        return HARD_THROUGH_LIMIT;
    }

    public void setHard_through_limit(String HARD_THROUGH_LIMIT) {
        this.HARD_THROUGH_LIMIT = HARD_THROUGH_LIMIT;
    }
    public String getMedium_through_limit() {
        return MEDIUM_THROUGH_LIMIT;
    }

    public void setMedium_through_limit(String MEDIUM_THROUGH_LIMIT) {
        this.MEDIUM_THROUGH_LIMIT = MEDIUM_THROUGH_LIMIT;
    }
    public String getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(String drawCount) {
        this.drawCount = drawCount;
    }


}