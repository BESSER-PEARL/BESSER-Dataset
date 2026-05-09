





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_IntegerLiteralExpCS extends PrimitiveLiteralExpCS {

    private String integerSymbol;



    public ocl_cst_IntegerLiteralExpCS(
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