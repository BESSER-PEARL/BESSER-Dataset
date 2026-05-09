





import java.util.List;
import java.util.ArrayList;

public class essentialocl_expressions_BooleanLiteralExp extends PrimitiveLiteralExp {

    private String booleanSymbol;



    public essentialocl_expressions_BooleanLiteralExp(
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