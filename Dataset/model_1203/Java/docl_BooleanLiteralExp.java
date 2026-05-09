





import java.util.List;
import java.util.ArrayList;

public class docl_BooleanLiteralExp extends PrimitiveExp {

    private String symbol;



    public docl_BooleanLiteralExp(
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