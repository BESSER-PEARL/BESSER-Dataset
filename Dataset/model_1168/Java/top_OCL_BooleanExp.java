





import java.util.List;
import java.util.ArrayList;

public class top_OCL_BooleanExp extends PrimitiveExp {

    private String booleanSymbol;



    public top_OCL_BooleanExp(
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