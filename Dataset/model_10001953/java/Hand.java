





import java.util.List;
import java.util.ArrayList;

public class Hand  {

    private None value;





    private List<Cards> cardss;




    private Player player;


    public Hand(
        None value    ) {
        this.value = value;
        this.cardss = new ArrayList<>();
    }

    public Hand(
        None value        ArrayList<Cards> cardss    ) {
        this.value = value;
        this.cardss = cardss;
    }

    public None getValue() {
        return value;
    }

    public void setValue(None value) {
        this.value = value;
    }

    public List<Cards> getCardss() {
        return cardss;
    }

    public void addCards(Cards cards) {
        this.cardss.add(cards);
    }
    public Player getPlayer() {
        return player;
    }

    public void setPlayer(Player player) {
        this.player = player;
    }

}