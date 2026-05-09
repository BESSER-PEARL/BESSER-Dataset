





import java.util.List;
import java.util.ArrayList;

public class ocl_expressions_IntegerLiteralExp  {

    private String extendedIntegerSymbol;
    private String longSymbol;
    private String integerSymbol;



    public ocl_expressions_IntegerLiteralExp(
        String extendedIntegerSymbol,        String longSymbol,        String integerSymbol    ) {
        this.extendedIntegerSymbol = extendedIntegerSymbol;
        this.longSymbol = longSymbol;
        this.integerSymbol = integerSymbol;
    }


    public String getExtendedintegersymbol() {
        return extendedIntegerSymbol;
    }

    public void setExtendedintegersymbol(String extendedIntegerSymbol) {
        this.extendedIntegerSymbol = extendedIntegerSymbol;
    }
    public String getLongsymbol() {
        return longSymbol;
    }

    public void setLongsymbol(String longSymbol) {
        this.longSymbol = longSymbol;
    }
    public String getIntegersymbol() {
        return integerSymbol;
    }

    public void setIntegersymbol(String integerSymbol) {
        this.integerSymbol = integerSymbol;
    }


}