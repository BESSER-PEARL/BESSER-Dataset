





import java.util.List;
import java.util.ArrayList;

public class typesystem_UnitFactor  {

    private int exponent;
    private String symbol;





    private typesystem_UnitProduct typesystem_unitproduct;


    public typesystem_UnitFactor(
        int exponent,        String symbol    ) {
        this.exponent = exponent;
        this.symbol = symbol;
    }


    public int getExponent() {
        return exponent;
    }

    public void setExponent(int exponent) {
        this.exponent = exponent;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public typesystem_UnitProduct getTypesystem_unitproduct() {
        return typesystem_unitproduct;
    }

    public void setTypesystem_unitproduct(typesystem_UnitProduct typesystem_unitproduct) {
        this.typesystem_unitproduct = typesystem_unitproduct;
    }

}