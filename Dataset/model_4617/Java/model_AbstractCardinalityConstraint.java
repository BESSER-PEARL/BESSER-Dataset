





import java.util.List;
import java.util.ArrayList;

public class model_AbstractCardinalityConstraint extends AbstractConstraint {

    private String cardMax;
    private String cardMin;



    public model_AbstractCardinalityConstraint(
        String cardMax,        String cardMin    ) {
        super(
        );
        this.cardMax = cardMax;
        this.cardMin = cardMin;
    }


    public String getCardmax() {
        return cardMax;
    }

    public void setCardmax(String cardMax) {
        this.cardMax = cardMax;
    }
    public String getCardmin() {
        return cardMin;
    }

    public void setCardmin(String cardMin) {
        this.cardMin = cardMin;
    }


}