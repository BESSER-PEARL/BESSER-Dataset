





import java.util.List;
import java.util.ArrayList;

public class OCL_StringLiteralExp extends PrimitiveLiteralExp {

    private String stringSymbol;



    public OCL_StringLiteralExp(
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