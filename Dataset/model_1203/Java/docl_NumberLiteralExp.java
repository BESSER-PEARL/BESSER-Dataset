





import java.util.List;
import java.util.ArrayList;

public class docl_NumberLiteralExp extends PrimitiveExp {

    private int symbol;



    public docl_NumberLiteralExp(
        int symbol    ) {
        super(
        );
        this.symbol = symbol;
    }


    public int getSymbol() {
        return symbol;
    }

    public void setSymbol(int symbol) {
        this.symbol = symbol;
    }


}