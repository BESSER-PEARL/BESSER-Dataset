





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_StringLiteralExpCS extends PrimitiveLiteralExpCS {

    private String stringSymbol;
    private String unescapedStringSymbol;



    public ocl_cst_StringLiteralExpCS(
        String stringSymbol,        String unescapedStringSymbol    ) {
        super(
        );
        this.stringSymbol = stringSymbol;
        this.unescapedStringSymbol = unescapedStringSymbol;
    }


    public String getStringsymbol() {
        return stringSymbol;
    }

    public void setStringsymbol(String stringSymbol) {
        this.stringSymbol = stringSymbol;
    }
    public String getUnescapedstringsymbol() {
        return unescapedStringSymbol;
    }

    public void setUnescapedstringsymbol(String unescapedStringSymbol) {
        this.unescapedStringSymbol = unescapedStringSymbol;
    }


}