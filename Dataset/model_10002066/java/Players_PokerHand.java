





import java.util.List;
import java.util.ArrayList;

public class Players_PokerHand  {

    private int value;
    private None highCard;
    private None Cards;





    private List<Cards_Card_Interface> cards_card_interfaces;




    private Players_Player players_player;


    public Players_PokerHand(
        int value,        None highCard,        None Cards    ) {
        this.value = value;
        this.highCard = highCard;
        this.Cards = Cards;
        this.cards_card_interfaces = new ArrayList<>();
    }

    public Players_PokerHand(
        int value,        None highCard,        None Cards        ArrayList<Cards_Card_Interface> cards_card_interfaces    ) {
        this.value = value;
        this.highCard = highCard;
        this.Cards = Cards;
        this.cards_card_interfaces = cards_card_interfaces;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public None getHighcard() {
        return highCard;
    }

    public void setHighcard(None highCard) {
        this.highCard = highCard;
    }
    public None getCards() {
        return Cards;
    }

    public void setCards(None Cards) {
        this.Cards = Cards;
    }

    public List<Cards_Card_Interface> getCards_card_interfaces() {
        return cards_card_interfaces;
    }

    public void addCards_card_interface(Cards_card_interface cards_card_interface) {
        this.cards_card_interfaces.add(cards_card_interface);
    }
    public Players_Player getPlayers_player() {
        return players_player;
    }

    public void setPlayers_player(Players_Player players_player) {
        this.players_player = players_player;
    }

}