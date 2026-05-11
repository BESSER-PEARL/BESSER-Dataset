





import java.util.List;
import java.util.ArrayList;

public class asmeta_basicterms_ConstantTerm extends BasicTerm {

    private String symbol;



    public asmeta_basicterms_ConstantTerm(
        String symbol    ) {
        super(
        );
        this.symbol = symbol;
    }


    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }


}