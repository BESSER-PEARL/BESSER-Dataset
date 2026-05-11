





import java.util.List;
import java.util.ArrayList;

public class typesystem_UnitFactor  {

    private String symbol;
    private int exponent;





    private typesystem_UnitProduct typesystem_unitproduct;


    public typesystem_UnitFactor(
        String symbol,        int exponent    ) {
        this.symbol = symbol;
        this.exponent = exponent;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public int getExponent() {
        return exponent;
    }

    public void setExponent(int exponent) {
        this.exponent = exponent;
    }

    public typesystem_UnitProduct getTypesystem_unitproduct() {
        return typesystem_unitproduct;
    }

    public void setTypesystem_unitproduct(typesystem_UnitProduct typesystem_unitproduct) {
        this.typesystem_unitproduct = typesystem_unitproduct;
    }

}