





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_StringLiteralExpCS extends PrimitiveLiteralExpCS {

    private String stringSymbol;



    public ocl_cst_StringLiteralExpCS(
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