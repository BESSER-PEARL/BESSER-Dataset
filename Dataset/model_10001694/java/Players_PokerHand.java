





import java.util.List;
import java.util.ArrayList;

public class Players_PokerHand  {

    private None highCard;
    private int value;
    private None Cards;





    private Players_Player players_player;




    private List<Cards_Card_Interface> cards_card_interfaces;


    public Players_PokerHand(
        None highCard,        int value,        None Cards    ) {
        this.highCard = highCard;
        this.value = value;
        this.Cards = Cards;
        this.cards_card_interfaces = new ArrayList<>();
    }

    public Players_PokerHand(
        None highCard,        int value,        None Cards        ArrayList<Cards_Card_Interface> cards_card_interfaces    ) {
        this.highCard = highCard;
        this.value = value;
        this.Cards = Cards;
        this.cards_card_interfaces = cards_card_interfaces;
    }

    public None getHighcard() {
        return highCard;
    }

    public void setHighcard(None highCard) {
        this.highCard = highCard;
    }
    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public None getCards() {
        return Cards;
    }

    public void setCards(None Cards) {
        this.Cards = Cards;
    }

    public Players_Player getPlayers_player() {
        return players_player;
    }

    public void setPlayers_player(Players_Player players_player) {
        this.players_player = players_player;
    }
    public List<Cards_Card_Interface> getCards_card_interfaces() {
        return cards_card_interfaces;
    }

    public void addCards_card_interface(Cards_card_interface cards_card_interface) {
        this.cards_card_interfaces.add(cards_card_interface);
    }

}