





import java.util.List;
import java.util.ArrayList;

public class ChangeAppearance  {

    private String backgrounds;
    private int deckNumber;
    private boolean exited;
    private int NUM_DECKS;
    private String cardBackLabel;
    private int FRS_DECK;
    private int backgroundNumber;
    private int NUM_BACKGROUNDS;
    private String decks;
    private String backgroundLabel;
    private String ok;
    private int FRS_BACKGROUND;



    public ChangeAppearance(
        String backgrounds,        int deckNumber,        boolean exited,        int NUM_DECKS,        String cardBackLabel,        int FRS_DECK,        int backgroundNumber,        int NUM_BACKGROUNDS,        String decks,        String backgroundLabel,        String ok,        int FRS_BACKGROUND    ) {
        this.backgrounds = backgrounds;
        this.deckNumber = deckNumber;
        this.exited = exited;
        this.NUM_DECKS = NUM_DECKS;
        this.cardBackLabel = cardBackLabel;
        this.FRS_DECK = FRS_DECK;
        this.backgroundNumber = backgroundNumber;
        this.NUM_BACKGROUNDS = NUM_BACKGROUNDS;
        this.decks = decks;
        this.backgroundLabel = backgroundLabel;
        this.ok = ok;
        this.FRS_BACKGROUND = FRS_BACKGROUND;
    }


    public String getBackgrounds() {
        return backgrounds;
    }

    public void setBackgrounds(String backgrounds) {
        this.backgrounds = backgrounds;
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
    public int getNum_decks() {
        return NUM_DECKS;
    }

    public void setNum_decks(int NUM_DECKS) {
        this.NUM_DECKS = NUM_DECKS;
    }
    public String getCardbacklabel() {
        return cardBackLabel;
    }

    public void setCardbacklabel(String cardBackLabel) {
        this.cardBackLabel = cardBackLabel;
    }
    public int getFrs_deck() {
        return FRS_DECK;
    }

    public void setFrs_deck(int FRS_DECK) {
        this.FRS_DECK = FRS_DECK;
    }
    public int getBackgroundnumber() {
        return backgroundNumber;
    }

    public void setBackgroundnumber(int backgroundNumber) {
        this.backgroundNumber = backgroundNumber;
    }
    public int getNum_backgrounds() {
        return NUM_BACKGROUNDS;
    }

    public void setNum_backgrounds(int NUM_BACKGROUNDS) {
        this.NUM_BACKGROUNDS = NUM_BACKGROUNDS;
    }
    public String getDecks() {
        return decks;
    }

    public void setDecks(String decks) {
        this.decks = decks;
    }
    public String getBackgroundlabel() {
        return backgroundLabel;
    }

    public void setBackgroundlabel(String backgroundLabel) {
        this.backgroundLabel = backgroundLabel;
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


}