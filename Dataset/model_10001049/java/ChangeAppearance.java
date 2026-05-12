





import java.util.List;
import java.util.ArrayList;

public class ChangeAppearance  {

    private String backgrounds;
    private int NUM_DECKS;
    private String ok;
    private int FRS_BACKGROUND;
    private int deckNumber;
    private boolean exited;
    private String decks;
    private int NUM_BACKGROUNDS;
    private String cardBackLabel;
    private int backgroundNumber;
    private String backgroundLabel;
    private int FRS_DECK;



    public ChangeAppearance(
        String backgrounds,        int NUM_DECKS,        String ok,        int FRS_BACKGROUND,        int deckNumber,        boolean exited,        String decks,        int NUM_BACKGROUNDS,        String cardBackLabel,        int backgroundNumber,        String backgroundLabel,        int FRS_DECK    ) {
        this.backgrounds = backgrounds;
        this.NUM_DECKS = NUM_DECKS;
        this.ok = ok;
        this.FRS_BACKGROUND = FRS_BACKGROUND;
        this.deckNumber = deckNumber;
        this.exited = exited;
        this.decks = decks;
        this.NUM_BACKGROUNDS = NUM_BACKGROUNDS;
        this.cardBackLabel = cardBackLabel;
        this.backgroundNumber = backgroundNumber;
        this.backgroundLabel = backgroundLabel;
        this.FRS_DECK = FRS_DECK;
    }


    public String getBackgrounds() {
        return backgrounds;
    }

    public void setBackgrounds(String backgrounds) {
        this.backgrounds = backgrounds;
    }
    public int getNum_decks() {
        return NUM_DECKS;
    }

    public void setNum_decks(int NUM_DECKS) {
        this.NUM_DECKS = NUM_DECKS;
    }
    public String getOk() {
        return ok;
    }

    public void setOk(String ok) {
        this.ok = ok;
    }
    public int getFrs_background() {
        return FRS_BACKGROUND;
    }

    public void setFrs_background(int FRS_BACKGROUND) {
        this.FRS_BACKGROUND = FRS_BACKGROUND;
    }
    public int getDecknumber() {
        return deckNumber;
    }

    public void setDecknumber(int deckNumber) {
        this.deckNumber = deckNumber;
    }
    public boolean getExited() {
        return exited;
    }

    public void setExited(boolean exited) {
        this.exited = exited;
    }
    public String getDecks() {
        return decks;
    }

    public void setDecks(String decks) {
        this.decks = decks;
    }
    public int getNum_backgrounds() {
        return NUM_BACKGROUNDS;
    }

    public void setNum_backgrounds(int NUM_BACKGROUNDS) {
        this.NUM_BACKGROUNDS = NUM_BACKGROUNDS;
    }
    public String getCardbacklabel() {
        return cardBackLabel;
    }

    public void setCardbacklabel(String cardBackLabel) {
        this.cardBackLabel = cardBackLabel;
    }
    public int getBackgroundnumber() {
        return backgroundNumber;
    }

    public void setBackgroundnumber(int backgroundNumber) {
        this.backgroundNumber = backgroundNumber;
    }
    public String getBackgroundlabel() {
        return backgroundLabel;
    }

    public void setBackgroundlabel(String backgroundLabel) {
        this.backgroundLabel = backgroundLabel;
    }
    public int getFrs_deck() {
        return FRS_DECK;
    }

    public void setFrs_deck(int FRS_DECK) {
        this.FRS_DECK = FRS_DECK;
    }


}