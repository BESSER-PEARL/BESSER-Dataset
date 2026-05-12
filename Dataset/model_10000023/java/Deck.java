





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private String shuffle__;
    private None deck__;
    private String draw__;
    private boolean isEmpty__;
    private int topcard;





    private WAR war;


    public Deck(
        String shuffle__,        None deck__,        String draw__,        boolean isEmpty__,        int topcard    ) {
        this.shuffle__ = shuffle__;
        this.deck__ = deck__;
        this.draw__ = draw__;
        this.isEmpty__ = isEmpty__;
        this.topcard = topcard;
    }


    public String getShuffle__() {
        return shuffle__;
    }

    public void setShuffle__(String shuffle__) {
        this.shuffle__ = shuffle__;
    }
    public None getDeck__() {
        return deck__;
    }

    public void setDeck__(None deck__) {
        this.deck__ = deck__;
    }
    public String getDraw__() {
        return draw__;
    }

    public void setDraw__(String draw__) {
        this.draw__ = draw__;
    }
    public boolean getIsempty__() {
        return isEmpty__;
    }

    public void setIsempty__(boolean isEmpty__) {
        this.isEmpty__ = isEmpty__;
    }
    public int getTopcard() {
        return topcard;
    }

    public void setTopcard(int topcard) {
        this.topcard = topcard;
    }

    public WAR getWar() {
        return war;
    }

    public void setWar(WAR war) {
        this.war = war;
    }

}