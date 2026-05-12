





import java.util.List;
import java.util.ArrayList;

public class CardTable  {

    private boolean done;
    private String stage;
    private None cards;



    public CardTable(
        boolean done,        String stage,        None cards    ) {
        this.done = done;
        this.stage = stage;
        this.cards = cards;
    }


    public boolean getDone() {
        return done;
    }

    public void setDone(boolean done) {
        this.done = done;
    }
    public String getStage() {
        return stage;
    }

    public void setStage(String stage) {
        this.stage = stage;
    }
    public None getCards() {
        return cards;
    }

    public void setCards(None cards) {
        this.cards = cards;
    }


}