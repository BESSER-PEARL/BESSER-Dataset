





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private int money;
    private String name;





    private Deck deck;


    public Player(
        int money,        String name    ) {
        this.money = money;
        this.name = name;
    }


    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}