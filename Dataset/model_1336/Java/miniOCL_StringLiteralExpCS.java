





import java.util.List;
import java.util.ArrayList;

public class miniOCL_StringLiteralExpCS extends LiteralExpCS {

    private String stringSymbol;



    public miniOCL_StringLiteralExpCS(
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