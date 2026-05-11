





import java.util.List;
import java.util.ArrayList;

public class MARTE_NFPs_Dimension  {

    private int baseExponent;
    private String symbol;



    public MARTE_NFPs_Dimension(
        int baseExponent,        String symbol    ) {
        this.baseExponent = baseExponent;
        this.symbol = symbol;
    }


    public int getBaseexponent() {
        return baseExponent;
    }

    public void setBaseexponent(int baseExponent) {
        this.baseExponent = baseExponent;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }


}