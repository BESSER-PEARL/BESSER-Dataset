





import java.util.List;
import java.util.ArrayList;

public class camel_provider_Cardinality  {

    private int cardinalityMax;
    private int cardinalityMin;



    public camel_provider_Cardinality(
        int cardinalityMax,        int cardinalityMin    ) {
        this.cardinalityMax = cardinalityMax;
        this.cardinalityMin = cardinalityMin;
    }


    public int getCardinalitymax() {
        return cardinalityMax;
    }

    public void setCardinalitymax(int cardinalityMax) {
        this.cardinalityMax = cardinalityMax;
    }
    public int getCardinalitymin() {
        return cardinalityMin;
    }

    public void setCardinalitymin(int cardinalityMin) {
        this.cardinalityMin = cardinalityMin;
    }


}