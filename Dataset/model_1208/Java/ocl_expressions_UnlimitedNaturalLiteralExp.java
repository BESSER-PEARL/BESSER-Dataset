





import java.util.List;
import java.util.ArrayList;

public class ocl_expressions_UnlimitedNaturalLiteralExp  {

    private String integerSymbol;
    private boolean unlimited;



    public ocl_expressions_UnlimitedNaturalLiteralExp(
        String integerSymbol,        boolean unlimited    ) {
        this.integerSymbol = integerSymbol;
        this.unlimited = unlimited;
    }


    public String getIntegersymbol() {
        return integerSymbol;
    }

    public void setIntegersymbol(String integerSymbol) {
        this.integerSymbol = integerSymbol;
    }
    public boolean getUnlimited() {
        return unlimited;
    }

    public void setUnlimited(boolean unlimited) {
        this.unlimited = unlimited;
    }


}