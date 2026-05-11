





import java.util.List;
import java.util.ArrayList;

public class gDSL_SelectExp extends MExp {

    private String symbol;



    public gDSL_SelectExp(
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