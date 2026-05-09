





import java.util.List;
import java.util.ArrayList;

public class atlstatic_OCL_StringExp extends PrimitiveExp {

    private String stringSymbol;



    public atlstatic_OCL_StringExp(
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