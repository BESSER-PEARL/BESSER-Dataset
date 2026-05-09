





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_PrimitiveLiteralExpCS extends LiteralExpCS {

    private String symbol;



    public ocl_cst_PrimitiveLiteralExpCS(
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