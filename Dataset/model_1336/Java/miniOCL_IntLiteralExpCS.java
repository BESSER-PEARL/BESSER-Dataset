





import java.util.List;
import java.util.ArrayList;

public class miniOCL_IntLiteralExpCS extends LiteralExpCS {

    private int intSymbol;



    public miniOCL_IntLiteralExpCS(
        int intSymbol    ) {
        super(
        );
        this.intSymbol = intSymbol;
    }


    public int getIntsymbol() {
        return intSymbol;
    }

    public void setIntsymbol(int intSymbol) {
        this.intSymbol = intSymbol;
    }


}