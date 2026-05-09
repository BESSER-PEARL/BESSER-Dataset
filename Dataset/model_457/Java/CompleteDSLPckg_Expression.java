





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_Expression extends ValueSpecification {

    private String symbol;





    private CompleteDSLPckg_ValueSpecification completedslpckg_valuespecification;


    public CompleteDSLPckg_Expression(
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

    public CompleteDSLPckg_ValueSpecification getCompletedslpckg_valuespecification() {
        return completedslpckg_valuespecification;
    }

    public void setCompletedslpckg_valuespecification(CompleteDSLPckg_ValueSpecification completedslpckg_valuespecification) {
        this.completedslpckg_valuespecification = completedslpckg_valuespecification;
    }

}