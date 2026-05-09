





import java.util.List;
import java.util.ArrayList;

public class superimposed_BooleanExp extends PrimitiveExp {

    private String booleanSymbol;



    public superimposed_BooleanExp(
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