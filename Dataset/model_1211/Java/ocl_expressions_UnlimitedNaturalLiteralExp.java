





import java.util.List;
import java.util.ArrayList;

public class ocl_expressions_UnlimitedNaturalLiteralExp  {

    private String extendedIntegerSymbol;
    private boolean unlimited;
    private String longSymbol;
    private String integerSymbol;



    public ocl_expressions_UnlimitedNaturalLiteralExp(
        String extendedIntegerSymbol,        boolean unlimited,        String longSymbol,        String integerSymbol    ) {
        this.extendedIntegerSymbol = extendedIntegerSymbol;
        this.unlimited = unlimited;
        this.longSymbol = longSymbol;
        this.integerSymbol = integerSymbol;
    }


    public String getExtendedintegersymbol() {
        return extendedIntegerSymbol;
    }

    public void setExtendedintegersymbol(String extendedIntegerSymbol) {
        this.extendedIntegerSymbol = extendedIntegerSymbol;
    }
    public boolean getUnlimited() {
        return unlimited;
    }

    public void setUnlimited(boolean unlimited) {
        this.unlimited = unlimited;
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