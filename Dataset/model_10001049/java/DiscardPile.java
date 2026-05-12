





import java.util.List;
import java.util.ArrayList;

public class DiscardPile  {

    private int cardsLeftFromDraw;
    private int drawCount;





    private DealDeck dealdeck;


    public DiscardPile(
        int cardsLeftFromDraw,        int drawCount    ) {
        this.cardsLeftFromDraw = cardsLeftFromDraw;
        this.drawCount = drawCount;
    }


    public int getCardsleftfromdraw() {
        return cardsLeftFromDraw;
    }

    public void setCardsleftfromdraw(int cardsLeftFromDraw) {
        this.cardsLeftFromDraw = cardsLeftFromDraw;
    }
    public int getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(int drawCount) {
        this.drawCount = drawCount;
    }

    public DealDeck getDealdeck() {
        return dealdeck;
    }

    public void setDealdeck(DealDeck dealdeck) {
        this.dealdeck = dealdeck;
    }

}