





import java.util.List;
import java.util.ArrayList;

public class operators_IntegerExp extends NumericExp {

    private String integerSymbol;



    public operators_IntegerExp(
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