





import java.util.List;
import java.util.ArrayList;

public class execTraces_RealLiteral extends Literal {

    private int intPart;
    private int decimalPart;



    public execTraces_RealLiteral(
        int intPart,        int decimalPart    ) {
        super(
        );
        this.intPart = intPart;
        this.decimalPart = decimalPart;
    }


    public int getIntpart() {
        return intPart;
    }

    public void setIntpart(int intPart) {
        this.intPart = intPart;
    }
    public int getDecimalpart() {
        return decimalPart;
    }

    public void setDecimalpart(int decimalPart) {
        this.decimalPart = decimalPart;
    }


}