





import java.util.List;
import java.util.ArrayList;

public class DealDeck  {

    private int numTimesThroughDeck;
    private int deckThroughLimit;
    private int difficulty;
    private boolean redealable;
    private int DRAW_ONE_THROUGH_LIMIT;
    private int drawCount;
    private int MEDIUM_THROUGH_LIMIT;
    private int EASY_THROUGH_LIMIT;
    private int HARD_THROUGH_LIMIT;
    private int DRAW_THREE_THROUGH_LIMIT;



    public DealDeck(
        int numTimesThroughDeck,        int deckThroughLimit,        int difficulty,        boolean redealable,        int DRAW_ONE_THROUGH_LIMIT,        int drawCount,        int MEDIUM_THROUGH_LIMIT,        int EASY_THROUGH_LIMIT,        int HARD_THROUGH_LIMIT,        int DRAW_THREE_THROUGH_LIMIT    ) {
        this.numTimesThroughDeck = numTimesThroughDeck;
        this.deckThroughLimit = deckThroughLimit;
        this.difficulty = difficulty;
        this.redealable = redealable;
        this.DRAW_ONE_THROUGH_LIMIT = DRAW_ONE_THROUGH_LIMIT;
        this.drawCount = drawCount;
        this.MEDIUM_THROUGH_LIMIT = MEDIUM_THROUGH_LIMIT;
        this.EASY_THROUGH_LIMIT = EASY_THROUGH_LIMIT;
        this.HARD_THROUGH_LIMIT = HARD_THROUGH_LIMIT;
        this.DRAW_THREE_THROUGH_LIMIT = DRAW_THREE_THROUGH_LIMIT;
    }


    public int getNumtimesthroughdeck() {
        return numTimesThroughDeck;
    }

    public void setNumtimesthroughdeck(int numTimesThroughDeck) {
        this.numTimesThroughDeck = numTimesThroughDeck;
    }
    public int getDeckthroughlimit() {
        return deckThroughLimit;
    }

    public void setDeckthroughlimit(int deckThroughLimit) {
        this.deckThroughLimit = deckThroughLimit;
    }
    public int getDifficulty() {
        return difficulty;
    }

    public void setDifficulty(int difficulty) {
        this.difficulty = difficulty;
    }
    public boolean getRedealable() {
        return redealable;
    }

    public void setRedealable(boolean redealable) {
        this.redealable = redealable;
    }
    public int getDraw_one_through_limit() {
        return DRAW_ONE_THROUGH_LIMIT;
    }

    public void setDraw_one_through_limit(int DRAW_ONE_THROUGH_LIMIT) {
        this.DRAW_ONE_THROUGH_LIMIT = DRAW_ONE_THROUGH_LIMIT;
    }
    public int getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(int drawCount) {
        this.drawCount = drawCount;
    }
    public int getMedium_through_limit() {
        return MEDIUM_THROUGH_LIMIT;
    }

    public void setMedium_through_limit(int MEDIUM_THROUGH_LIMIT) {
        this.MEDIUM_THROUGH_LIMIT = MEDIUM_THROUGH_LIMIT;
    }
    public int getEasy_through_limit() {
        return EASY_THROUGH_LIMIT;
    }

    public void setEasy_through_limit(int EASY_THROUGH_LIMIT) {
        this.EASY_THROUGH_LIMIT = EASY_THROUGH_LIMIT;
    }
    public int getHard_through_limit() {
        return HARD_THROUGH_LIMIT;
    }

    public void setHard_through_limit(int HARD_THROUGH_LIMIT) {
        this.HARD_THROUGH_LIMIT = HARD_THROUGH_LIMIT;
    }
    public int getDraw_three_through_limit() {
        return DRAW_THREE_THROUGH_LIMIT;
    }

    public void setDraw_three_through_limit(int DRAW_THREE_THROUGH_LIMIT) {
        this.DRAW_THREE_THROUGH_LIMIT = DRAW_THREE_THROUGH_LIMIT;
    }


}