





import java.util.List;
import java.util.ArrayList;

public class OCL_BooleanLiteralExp extends PrimitiveLiteralExp {

    private String booleanSymbol;



    public OCL_BooleanLiteralExp(
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