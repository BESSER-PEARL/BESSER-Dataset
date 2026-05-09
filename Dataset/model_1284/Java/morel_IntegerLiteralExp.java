





import java.util.List;
import java.util.ArrayList;

public class morel_IntegerLiteralExp extends LiteralExp {

    private int integerSymbol;



    public morel_IntegerLiteralExp(
        int integerSymbol    ) {
        super(
        );
        this.integerSymbol = integerSymbol;
    }


    public int getIntegersymbol() {
        return integerSymbol;
    }

    public void setIntegersymbol(int integerSymbol) {
        this.integerSymbol = integerSymbol;
    }


}