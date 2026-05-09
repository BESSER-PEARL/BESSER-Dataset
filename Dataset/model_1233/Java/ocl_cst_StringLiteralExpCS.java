





import java.util.List;
import java.util.ArrayList;

public class ocl_cst_StringLiteralExpCS extends PrimitiveLiteralExpCS {

    private String unescapedStringSymbol;
    private String stringSymbol;



    public ocl_cst_StringLiteralExpCS(
        String unescapedStringSymbol,        String stringSymbol    ) {
        super(
        );
        this.unescapedStringSymbol = unescapedStringSymbol;
        this.stringSymbol = stringSymbol;
    }


    public String getUnescapedstringsymbol() {
        return unescapedStringSymbol;
    }

    public void setUnescapedstringsymbol(String unescapedStringSymbol) {
        this.unescapedStringSymbol = unescapedStringSymbol;
    }
    public String getStringsymbol() {
        return stringSymbol;
    }

    public void setStringsymbol(String stringSymbol) {
        this.stringSymbol = stringSymbol;
    }


}