





import java.util.List;
import java.util.ArrayList;

public class optGrammar_SymbolAlias  {

    private String symbol;
    private String alias;





    private optGrammar_ImportDirective optgrammar_importdirective;


    public optGrammar_SymbolAlias(
        String symbol,        String alias    ) {
        this.symbol = symbol;
        this.alias = alias;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public optGrammar_ImportDirective getOptgrammar_importdirective() {
        return optgrammar_importdirective;
    }

    public void setOptgrammar_importdirective(optGrammar_ImportDirective optgrammar_importdirective) {
        this.optgrammar_importdirective = optgrammar_importdirective;
    }

}