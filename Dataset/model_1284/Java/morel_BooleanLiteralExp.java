





import java.util.List;
import java.util.ArrayList;

public class morel_BooleanLiteralExp extends LiteralExp {

    private boolean boolSymbol;



    public morel_BooleanLiteralExp(
        boolean boolSymbol    ) {
        super(
        );
        this.boolSymbol = boolSymbol;
    }


    public boolean getBoolsymbol() {
        return boolSymbol;
    }

    public void setBoolsymbol(boolean boolSymbol) {
        this.boolSymbol = boolSymbol;
    }


}