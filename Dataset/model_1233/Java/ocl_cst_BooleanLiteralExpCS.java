





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_BooleanLiteralExpCS extends PrimitiveLiteralExpCS {

    private String booleanSymbol;



    public ocl_cst_BooleanLiteralExpCS(
        String booleanSymbol    ) {
        super(
        );
        this.booleanSymbol = booleanSymbol;
    }


    public String getBooleansymbol() {
        return booleanSymbol;
    }

    public void setBooleansymbol(String booleanSymbol) {
        this.booleanSymbol = booleanSymbol;
    }


}