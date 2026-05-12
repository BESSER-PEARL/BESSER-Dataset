





import java.util.List;
import java.util.ArrayList;

public class ChangeAppearance  {

    private String cardBackLabel;
    private String backgrounds;
    private String deckNumber;
    private String FRS_BACKGROUND;
    private boolean exited;
    private String NUM_BACKGROUNDS;
    private String backGroundLabel;
    private String backgroundNumber;
    private String decks;
    private String ok;
    private String NUM_DECKS;
    private String FRS_DECK;



    public ChangeAppearance(
        String cardBackLabel,        String backgrounds,        String deckNumber,        String FRS_BACKGROUND,        boolean exited,        String NUM_BACKGROUNDS,        String backGroundLabel,        String backgroundNumber,        String decks,        String ok,        String NUM_DECKS,        String FRS_DECK    ) {
        this.cardBackLabel = cardBackLabel;
        this.backgrounds = backgrounds;
        this.deckNumber = deckNumber;
        this.FRS_BACKGROUND = FRS_BACKGROUND;
        this.exited = exited;
        this.NUM_BACKGROUNDS = NUM_BACKGROUNDS;
        this.backGroundLabel = backGroundLabel;
        this.backgroundNumber = backgroundNumber;
        this.decks = decks;
        this.ok = ok;
        this.NUM_DECKS = NUM_DECKS;
        this.FRS_DECK = FRS_DECK;
    }


    public String getCardbacklabel() {
        return cardBackLabel;
    }

    public void setCardbacklabel(String cardBackLabel) {
        this.cardBackLabel = cardBackLabel;
    }
    public String getBackgrounds() {
        return backgrounds;
    }

    public void setBackgrounds(String backgrounds) {
        this.backgrounds = backgrounds;
    }
    public String getDecknumber() {
        return deckNumber;
    }

    public void setDecknumber(String deckNumber) {
        this.deckNumber = deckNumber;
    }
    public String getFrs_background() {
        return FRS_BACKGROUND;
    }

    public void setFrs_background(String FRS_BACKGROUND) {
        this.FRS_BACKGROUND = FRS_BACKGROUND;
    }
    public boolean getExited() {
        return exited;
    }

    public void setExited(boolean exited) {
        this.exited = exited;
    }
    public String getNum_backgrounds() {
        return NUM_BACKGROUNDS;
    }

    public void setNum_backgrounds(String NUM_BACKGROUNDS) {
        this.NUM_BACKGROUNDS = NUM_BACKGROUNDS;
    }
    public String getBackgroundlabel() {
        return backGroundLabel;
    }

    public void setBackgroundlabel(String backGroundLabel) {
        this.backGroundLabel = backGroundLabel;
    }
    public String getBackgroundnumber() {
        return backgroundNumber;
    }

    public void setBackgroundnumber(String backgroundNumber) {
        this.backgroundNumber = backgroundNumber;
    }
    public String getDecks() {
        return decks;
    }

    public void setDecks(String decks) {
        this.decks = decks;
    }
    public String getOk() {
        return ok;
    }

    public void setOk(String ok) {
        this.ok = ok;
    }
    public String getNum_decks() {
        return NUM_DECKS;
    }

    public void setNum_decks(String NUM_DECKS) {
        this.NUM_DECKS = NUM_DECKS;
    }
    public String getFrs_deck() {
        return FRS_DECK;
    }

    public void setFrs_deck(String FRS_DECK) {
        this.FRS_DECK = FRS_DECK;
    }


}