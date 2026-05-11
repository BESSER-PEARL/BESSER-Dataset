





import java.util.List;
import java.util.ArrayList;

public class MARTE_Operators_Operator  {

    private String symbol;
    private String arity;



    public MARTE_Operators_Operator(
        String symbol,        String arity    ) {
        this.symbol = symbol;
        this.arity = arity;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public String getArity() {
        return arity;
    }

    public void setArity(String arity) {
        this.arity = arity;
    }


}