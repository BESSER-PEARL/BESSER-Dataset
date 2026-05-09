





import java.util.List;
import java.util.ArrayList;

public class simpleocl_BooleanExp extends PrimitiveExp {

    private String booleanSymbol;



    public simpleocl_BooleanExp(
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