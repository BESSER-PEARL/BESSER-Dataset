





import java.util.List;
import java.util.ArrayList;

public class Player  {

    private String name;
    private int money;





    private Deck deck;


    public Player(
        String name,        int money    ) {
        this.name = name;
        this.money = money;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMoney() {
        return money;
    }

    public void setMoney(int money) {
        this.money = money;
    }

    public Deck getDeck() {
        return deck;
    }

    public void setDeck(Deck deck) {
        this.deck = deck;
    }

}