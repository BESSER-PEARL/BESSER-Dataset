





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_IntegerExp extends NumericExp {

    private String integerSymbol;



    public gbind_simpleocl_IntegerExp(
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