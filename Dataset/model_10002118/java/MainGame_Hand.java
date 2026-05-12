





import java.util.List;
import java.util.ArrayList;

public class MainGame_Hand  {

    private boolean straight;
    private boolean fourKind;
    private boolean straightFlush;
    private boolean highCard;
    private boolean fullHouse;
    private boolean threeKing;
    private boolean twoPair;
    private String Hand;
    private boolean flush;
    private boolean onePair;





    private List<Cards_Card> cards_cards;




    private Players_Player players_player;


    public MainGame_Hand(
        boolean straight,        boolean fourKind,        boolean straightFlush,        boolean highCard,        boolean fullHouse,        boolean threeKing,        boolean twoPair,        String Hand,        boolean flush,        boolean onePair    ) {
        this.straight = straight;
        this.fourKind = fourKind;
        this.straightFlush = straightFlush;
        this.highCard = highCard;
        this.fullHouse = fullHouse;
        this.threeKing = threeKing;
        this.twoPair = twoPair;
        this.Hand = Hand;
        this.flush = flush;
        this.onePair = onePair;
        this.cards_cards = new ArrayList<>();
    }

    public MainGame_Hand(
        boolean straight,        boolean fourKind,        boolean straightFlush,        boolean highCard,        boolean fullHouse,        boolean threeKing,        boolean twoPair,        String Hand,        boolean flush,        boolean onePair        ArrayList<Cards_Card> cards_cards    ) {
        this.straight = straight;
        this.fourKind = fourKind;
        this.straightFlush = straightFlush;
        this.highCard = highCard;
        this.fullHouse = fullHouse;
        this.threeKing = threeKing;
        this.twoPair = twoPair;
        this.Hand = Hand;
        this.flush = flush;
        this.onePair = onePair;
        this.cards_cards = cards_cards;
    }

    public boolean getStraight() {
        return straight;
    }

    public void setStraight(boolean straight) {
        this.straight = straight;
    }
    public boolean getFourkind() {
        return fourKind;
    }

    public void setFourkind(boolean fourKind) {
        this.fourKind = fourKind;
    }
    public boolean getStraightflush() {
        return straightFlush;
    }

    public void setStraightflush(boolean straightFlush) {
        this.straightFlush = straightFlush;
    }
    public boolean getHighcard() {
        return highCard;
    }

    public void setHighcard(boolean highCard) {
        this.highCard = highCard;
    }
    public boolean getFullhouse() {
        return fullHouse;
    }

    public void setFullhouse(boolean fullHouse) {
        this.fullHouse = fullHouse;
    }
    public boolean getThreeking() {
        return threeKing;
    }

    public void setThreeking(boolean threeKing) {
        this.threeKing = threeKing;
    }
    public boolean getTwopair() {
        return twoPair;
    }

    public void setTwopair(boolean twoPair) {
        this.twoPair = twoPair;
    }
    public String getHand() {
        return Hand;
    }

    public void setHand(String Hand) {
        this.Hand = Hand;
    }
    public boolean getFlush() {
        return flush;
    }

    public void setFlush(boolean flush) {
        this.flush = flush;
    }
    public boolean getOnepair() {
        return onePair;
    }

    public void setOnepair(boolean onePair) {
        this.onePair = onePair;
    }

    public List<Cards_Card> getCards_cards() {
        return cards_cards;
    }

    public void addCards_card(Cards_card cards_card) {
        this.cards_cards.add(cards_card);
    }
    public Players_Player getPlayers_player() {
        return players_player;
    }

    public void setPlayers_player(Players_Player players_player) {
        this.players_player = players_player;
    }

}