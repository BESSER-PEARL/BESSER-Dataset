





import java.util.List;
import java.util.ArrayList;

public class whileDsl_ExprSimpleWithSymbolLExpr  {

    private String symbol;





    private whileDsl_LExpr whiledsl_lexpr;


    public whileDsl_ExprSimpleWithSymbolLExpr(
        String symbol    ) {
        this.symbol = symbol;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public whileDsl_LExpr getWhiledsl_lexpr() {
        return whiledsl_lexpr;
    }

    public void setWhiledsl_lexpr(whileDsl_LExpr whiledsl_lexpr) {
        this.whiledsl_lexpr = whiledsl_lexpr;
    }

}