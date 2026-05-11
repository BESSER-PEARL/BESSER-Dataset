





import java.util.List;
import java.util.ArrayList;

public class operators_StringExp extends PrimitiveExp {

    private String stringSymbol;



    public operators_StringExp(
        String stringSymbol    ) {
        super(
        );
        this.stringSymbol = stringSymbol;
    }


    public String getStringsymbol() {
        return stringSymbol;
    }

    public void setStringsymbol(String stringSymbol) {
        this.stringSymbol = stringSymbol;
    }


}