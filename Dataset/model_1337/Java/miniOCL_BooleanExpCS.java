





import java.util.List;
import java.util.ArrayList;

public class miniOCL_BooleanExpCS extends BooleanLiteralExpCS {

    private boolean boolSymbol;



    public miniOCL_BooleanExpCS(
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