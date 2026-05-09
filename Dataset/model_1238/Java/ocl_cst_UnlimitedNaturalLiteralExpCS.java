





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_UnlimitedNaturalLiteralExpCS extends PrimitiveLiteralExpCS {

    private String extendedIntegerSymbol;
    private String integerSymbol;
    private String longSymbol;



    public ocl_cst_UnlimitedNaturalLiteralExpCS(
        String extendedIntegerSymbol,        String integerSymbol,        String longSymbol    ) {
        super(
        );
        this.extendedIntegerSymbol = extendedIntegerSymbol;
        this.integerSymbol = integerSymbol;
        this.longSymbol = longSymbol;
    }


    public String getExtendedintegersymbol() {
        return extendedIntegerSymbol;
    }

    public void setExtendedintegersymbol(String extendedIntegerSymbol) {
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


}