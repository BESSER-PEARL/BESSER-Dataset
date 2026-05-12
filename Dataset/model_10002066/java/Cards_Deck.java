





import java.util.List;
import java.util.ArrayList;

public class Cards_Deck  {

    private None burnt;
    private String list;





    private List<Cards_Card_Interface> cards_card_interfaces;


    public Cards_Deck(
        None burnt,        String list    ) {
        this.burnt = burnt;
        this.list = list;
        this.cards_card_interfaces = new ArrayList<>();
    }

    public Cards_Deck(
        None burnt,        String list        ArrayList<Cards_Card_Interface> cards_card_interfaces    ) {
        this.burnt = burnt;
        this.list = list;
        this.cards_card_interfaces = cards_card_interfaces;
    }

    public None getBurnt() {
        return burnt;
    }

    public void setBurnt(None burnt) {
        this.burnt = burnt;
    }
    public String getList() {
        return list;
    }

    public void setList(String list) {
        this.list = list;
    }

    public List<Cards_Card_Interface> getCards_card_interfaces() {
        return cards_card_interfaces;
    }

    public void addCards_card_interface(Cards_card_interface cards_card_interface) {
        this.cards_card_interfaces.add(cards_card_interface);
    }

}