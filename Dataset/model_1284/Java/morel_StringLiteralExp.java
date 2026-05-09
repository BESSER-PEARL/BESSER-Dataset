





import java.util.List;
import java.util.ArrayList;

public class morel_StringLiteralExp extends LiteralExp {

    private String stringSymbol;



    public morel_StringLiteralExp(
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