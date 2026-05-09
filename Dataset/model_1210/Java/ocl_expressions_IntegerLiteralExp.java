





import java.util.List;
import java.util.ArrayList;

public class ocl_expressions_IntegerLiteralExp  {

    private String integerSymbol;
    private String longSymbol;
    private String extendedIntegerSymbol;



    public ocl_expressions_IntegerLiteralExp(
        String integerSymbol,        String longSymbol,        String extendedIntegerSymbol    ) {
        this.integerSymbol = integerSymbol;
        this.longSymbol = longSymbol;
        this.extendedIntegerSymbol = extendedIntegerSymbol;
    }


    public String getIntegersymbol() {
        return integerSymbol;
    }

    public void setIntegersymbol(String integerSymbol) {
        this.integerSymbol = integerSymbol;
    }
    public String getLongsymbol() {
        return longSymbol;
    }

    public void setLongsymbol(String longSymbol) {
        this.longSymbol = longSymbol;
    }
    public String getExtendedintegersymbol() {
        return extendedIntegerSymbol;
    }

    public void setExtendedintegersymbol(String extendedIntegerSymbol) {
        this.extendedIntegerSymbol = extendedIntegerSymbol;
    }


}