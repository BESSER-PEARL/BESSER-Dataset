





import java.util.List;
import java.util.ArrayList;

public class EFM_Cardinality  {

    private int cardinalityMin;
    private int cardinalityMax;
    private int configValue;



    public EFM_Cardinality(
        int cardinalityMin,        int cardinalityMax,        int configValue    ) {
        this.cardinalityMin = cardinalityMin;
        this.cardinalityMax = cardinalityMax;
        this.configValue = configValue;
    }


    public int getCardinalitymin() {
        return cardinalityMin;
    }

    public void setCardinalitymin(int cardinalityMin) {
        this.cardinalityMin = cardinalityMin;
    }
    public int getCardinalitymax() {
        return cardinalityMax;
    }

    public void setCardinalitymax(int cardinalityMax) {
        this.cardinalityMax = cardinalityMax;
    }
    public int getConfigvalue() {
        return configValue;
    }

    public void setConfigvalue(int configValue) {
        this.configValue = configValue;
    }


}