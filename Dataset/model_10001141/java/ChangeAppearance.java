





import java.util.List;
import java.util.ArrayList;

public class ChangeAppearance  {

    private boolean exited;
    private String backgroundNumber;
    private String deckNumber;
    private String NUM_BACKGROUNDS;
    private String decks;
    private String backgrounds;
    private String FRS_DECK;
    private String ok;
    private String cardBackLabel;
    private String backGroundLabel;
    private String FRS_BACKGROUND;
    private String NUM_DECKS;



    public ChangeAppearance(
        boolean exited,        String backgroundNumber,        String deckNumber,        String NUM_BACKGROUNDS,        String decks,        String backgrounds,        String FRS_DECK,        String ok,        String cardBackLabel,        String backGroundLabel,        String FRS_BACKGROUND,        String NUM_DECKS    ) {
        this.exited = exited;
        this.backgroundNumber = backgroundNumber;
        this.deckNumber = deckNumber;
        this.NUM_BACKGROUNDS = NUM_BACKGROUNDS;
        this.decks = decks;
        this.backgrounds = backgrounds;
        this.FRS_DECK = FRS_DECK;
        this.ok = ok;
        this.cardBackLabel = cardBackLabel;
        this.backGroundLabel = backGroundLabel;
        this.FRS_BACKGROUND = FRS_BACKGROUND;
        this.NUM_DECKS = NUM_DECKS;
    }


    public boolean getExited() {
        return exited;
    }

    public void setExited(boolean exited) {
        this.exited = exited;
    }
    public String getBackgroundnumber() {
        return backgroundNumber;
    }

    public void setBackgroundnumber(String backgroundNumber) {
        this.backgroundNumber = backgroundNumber;
    }
    public String getDecknumber() {
        return deckNumber;
    }

    public void setDecknumber(String deckNumber) {
        this.deckNumber = deckNumber;
    }
    public String getNum_backgrounds() {
        return NUM_BACKGROUNDS;
    }

    public void setNum_backgrounds(String NUM_BACKGROUNDS) {
        this.NUM_BACKGROUNDS = NUM_BACKGROUNDS;
    }
    public String getDecks() {
        return decks;
    }

    public void setDecks(String decks) {
        this.decks = decks;
    }
    public String getBackgrounds() {
        return backgrounds;
    }

    public void setBackgrounds(String backgrounds) {
        this.backgrounds = backgrounds;
    }
    public String getFrs_deck() {
        return FRS_DECK;
    }

    public void setFrs_deck(String FRS_DECK) {
        this.FRS_DECK = FRS_DECK;
    }
    public String getOk() {
        return ok;
    }

    public void setOk(String ok) {
        this.ok = ok;
    }
    public String getCardbacklabel() {
        return cardBackLabel;
    }

    public void setCardbacklabel(String cardBackLabel) {
        this.cardBackLabel = cardBackLabel;
    }
    public String getBackgroundlabel() {
        return backGroundLabel;
    }

    public void setBackgroundlabel(String backGroundLabel) {
        this.backGroundLabel = backGroundLabel;
    }
    public String getFrs_background() {
        return FRS_BACKGROUND;
    }

    public void setFrs_background(String FRS_BACKGROUND) {
        this.FRS_BACKGROUND = FRS_BACKGROUND;
    }
    public String getNum_decks() {
        return NUM_DECKS;
    }

    public void setNum_decks(String NUM_DECKS) {
        this.NUM_DECKS = NUM_DECKS;
    }


}