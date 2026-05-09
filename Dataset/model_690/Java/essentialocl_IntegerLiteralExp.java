





import java.util.List;
import java.util.ArrayList;

public class essentialocl_IntegerLiteralExp extends NumericLiteralExp {

    private String integerSymbol;



    public essentialocl_IntegerLiteralExp(
        String integerSymbol    ) {
        super(
        );
        this.integerSymbol = integerSymbol;
    }


    public String getIntegersymbol() {
        return integerSymbol;
    }

    public void setIntegersymbol(String integerSymbol) {
        this.integerSymbol = integerSymbol;
    }


}