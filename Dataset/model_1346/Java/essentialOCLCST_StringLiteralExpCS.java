





import java.util.List;
import java.util.ArrayList;

public class essentialOCLCST_StringLiteralExpCS extends PrimitiveLiteralExpCS {

    private String stringSymbol;



    public essentialOCLCST_StringLiteralExpCS(
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