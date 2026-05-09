





import java.util.List;
import java.util.ArrayList;

public class ocl_expressions_UnlimitedNaturalLiteralExp  {

    private boolean unlimited;
    private String integerSymbol;



    public ocl_expressions_UnlimitedNaturalLiteralExp(
        boolean unlimited,        String integerSymbol    ) {
        this.unlimited = unlimited;
        this.integerSymbol = integerSymbol;
    }


    public boolean getUnlimited() {
        return unlimited;
    }

    public void setUnlimited(boolean unlimited) {
        this.unlimited = unlimited;
    }
    public String getIntegersymbol() {
        return integerSymbol;
    }

    public void setIntegersymbol(String integerSymbol) {
        this.integerSymbol = integerSymbol;
    }


}