





import java.util.List;
import java.util.ArrayList;

public class CardDeckInterface  {

    private int size;
    private String shuffle;
    private None draw;





    private Card card;


    public CardDeckInterface(
        int size,        String shuffle,        None draw    ) {
        this.size = size;
        this.shuffle = shuffle;
        this.draw = draw;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getShuffle() {
        return shuffle;
    }

    public void setShuffle(String shuffle) {
        this.shuffle = shuffle;
    }
    public None getDraw() {
        return draw;
    }

    public void setDraw(None draw) {
        this.draw = draw;
    }

    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }

}