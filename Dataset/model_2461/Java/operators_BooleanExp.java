





import java.util.List;
import java.util.ArrayList;

public class operators_BooleanExp extends PrimitiveExp {

    private String booleanSymbol;



    public operators_BooleanExp(
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