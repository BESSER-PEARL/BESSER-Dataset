





import java.util.List;
import java.util.ArrayList;

public class OCL_IntegerLiteralExp extends NumericLiteralExp {

    private String integerSymbol;



    public OCL_IntegerLiteralExp(
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