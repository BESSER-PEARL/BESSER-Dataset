





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_IntegerLiteralExpCS extends PrimitiveLiteralExpCS {

    private String longSymbol;
    private String integerSymbol;
    private String extendedIntegerSymbol;



    public ocl_cst_IntegerLiteralExpCS(
        String longSymbol,        String integerSymbol,        String extendedIntegerSymbol    ) {
        super(
        );
        this.longSymbol = longSymbol;
        this.integerSymbol = integerSymbol;
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
    public String getExtendedintegersymbol() {
        return extendedIntegerSymbol;
    }

    public void setExtendedintegersymbol(String extendedIntegerSymbol) {
        this.extendedIntegerSymbol = extendedIntegerSymbol;
    }


}