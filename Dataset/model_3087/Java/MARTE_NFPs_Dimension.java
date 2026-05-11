





import java.util.List;
import java.util.ArrayList;

public class MARTE_NFPs_Dimension  {

    private String symbol;
    private int baseExponent;



    public MARTE_NFPs_Dimension(
        String symbol,        int baseExponent    ) {
        this.symbol = symbol;
        this.baseExponent = baseExponent;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public int getBaseexponent() {
        return baseExponent;
    }

    public void setBaseexponent(int baseExponent) {
        this.baseExponent = baseExponent;
    }


}