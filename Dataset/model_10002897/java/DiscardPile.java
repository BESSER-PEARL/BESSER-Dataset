





import java.util.List;
import java.util.ArrayList;

public class DiscardPile  {

    private int drawCount;
    private int cardsLeftFromDraw;





    private DealDeck dealdeck;


    public DiscardPile(
        int drawCount,        int cardsLeftFromDraw    ) {
        this.drawCount = drawCount;
        this.cardsLeftFromDraw = cardsLeftFromDraw;
    }


    public int getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(int drawCount) {
        this.drawCount = drawCount;
    }
    public int getCardsleftfromdraw() {
        return cardsLeftFromDraw;
    }

    public void setCardsleftfromdraw(int cardsLeftFromDraw) {
        this.cardsLeftFromDraw = cardsLeftFromDraw;
    }

    public DealDeck getDealdeck() {
        return dealdeck;
    }

    public void setDealdeck(DealDeck dealdeck) {
        this.dealdeck = dealdeck;
    }

}