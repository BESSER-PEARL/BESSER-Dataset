





import java.util.List;
import java.util.ArrayList;

public class Game  {

    private int pot;
    private int bigBlindValue;
    private String players;
    private None currentDeck;
    private None currentCommunityCards;
    private int currentBigBlind;





    private CommunityCards communitycards;




    private Deck deck;




    private Player player;


    public Game(
        int pot,        int bigBlindValue,        String players,        None currentDeck,        None currentCommunityCards,        int currentBigBlind    ) {
        this.pot = pot;
        this.bigBlindValue = bigBlindValue;
        this.players = players;
        this.currentDeck = currentDeck;
        this.currentCommunityCards = currentCommunityCards;
        this.currentBigBlind = currentBigBlind;
    }


    public int getPot() {
        return pot;
    }

    public void setPot(int pot) {
        this.pot = pot;
    }
    public int getBigblindvalue() {
        return bigBlindValue;
    }

    public void setBigblindvalue(int bigBlindValue) {
        this.bigBlindValue = bigBlindValue;
    }
    public String getPlayers() {
        return players;
    }

    public void setPlayers(String players) {
        this.players = players;
    }
    public None getCurrentdeck() {
        return currentDeck;
    }

    public void setCurrentdeck(None currentDeck) {
        this.currentDeck = currentDeck;
    }
    public None getCurrentcommunitycards() {
        return currentCommunityCards;
    }

    public void setCurrentcommunitycards(None currentCommunityCards) {
        this.currentCommunityCards = currentCommunityCards;
    }
    public int getCurrentbigblind() {
        return currentBigBlind;
    }

    public void setCurrentbigblind(int currentBigBlind) {
        this.currentBigBlind = currentBigBlind;
    }

    public CommunityCards getCommunitycards() {
        return communitycards;
    }

    public void setCommunitycards(CommunityCards communitycards) {
        this.communitycards = communitycards;
    }
    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}