





import java.util.List;
import java.util.ArrayList;

public class DiscardPile  {

    private String drawCount;
    private String CardsLeftFromDraw;



    public DiscardPile(
        String drawCount,        String CardsLeftFromDraw    ) {
        this.drawCount = drawCount;
        this.CardsLeftFromDraw = CardsLeftFromDraw;
    }


    public String getDrawcount() {
        return drawCount;
    }

    public void setDrawcount(String drawCount) {
        this.drawCount = drawCount;
    }
    public String getCardsleftfromdraw() {
        return CardsLeftFromDraw;
    }

    public void setCardsleftfromdraw(String CardsLeftFromDraw) {
        this.CardsLeftFromDraw = CardsLeftFromDraw;
    }


}