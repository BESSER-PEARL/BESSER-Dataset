





import java.util.List;
import java.util.ArrayList;

public class Hand  {

    private boolean blackjack;
    private String hand;
    private String under;
    private boolean must_hit;
    private int num_card;
    private String busted;
    private int max_cards;
    private String bestscore;
    private String addcard;



    public Hand(
        boolean blackjack,        String hand,        String under,        boolean must_hit,        int num_card,        String busted,        int max_cards,        String bestscore,        String addcard    ) {
        this.blackjack = blackjack;
        this.hand = hand;
        this.under = under;
        this.must_hit = must_hit;
        this.num_card = num_card;
        this.busted = busted;
        this.max_cards = max_cards;
        this.bestscore = bestscore;
        this.addcard = addcard;
    }


    public boolean getBlackjack() {
        return blackjack;
    }

    public void setBlackjack(boolean blackjack) {
        this.blackjack = blackjack;
    }
    public String getHand() {
        return hand;
    }

    public void setHand(String hand) {
        this.hand = hand;
    }
    public String getUnder() {
        return under;
    }

    public void setUnder(String under) {
        this.under = under;
    }
    public boolean getMust_hit() {
        return must_hit;
    }

    public void setMust_hit(boolean must_hit) {
        this.must_hit = must_hit;
    }
    public int getNum_card() {
        return num_card;
    }

    public void setNum_card(int num_card) {
        this.num_card = num_card;
    }
    public String getBusted() {
        return busted;
    }

    public void setBusted(String busted) {
        this.busted = busted;
    }
    public int getMax_cards() {
        return max_cards;
    }

    public void setMax_cards(int max_cards) {
        this.max_cards = max_cards;
    }
    public String getBestscore() {
        return bestscore;
    }

    public void setBestscore(String bestscore) {
        this.bestscore = bestscore;
    }
    public String getAddcard() {
        return addcard;
    }

    public void setAddcard(String addcard) {
        this.addcard = addcard;
    }


}