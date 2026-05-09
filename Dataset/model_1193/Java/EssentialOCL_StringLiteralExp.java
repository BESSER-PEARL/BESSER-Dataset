





import java.util.List;
import java.util.ArrayList;

public class EssentialOCL_StringLiteralExp extends PrimitiveLiteralExp {

    private String stringSymbol;



    public EssentialOCL_StringLiteralExp(
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