





import java.util.List;
import java.util.ArrayList;

public class aDSL_IntegerNegative  {

    private int value;
    private boolean isneg;





    private aDSL_IntConstant adsl_intconstant;


    public aDSL_IntegerNegative(
        int value,        boolean isneg    ) {
        this.value = value;
        this.isneg = isneg;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }
    public boolean getIsneg() {
        return isneg;
    }

    public void setIsneg(boolean isneg) {
        this.isneg = isneg;
    }

    public aDSL_IntConstant getAdsl_intconstant() {
        return adsl_intconstant;
    }

    public void setAdsl_intconstant(aDSL_IntConstant adsl_intconstant) {
        this.adsl_intconstant = adsl_intconstant;
    }

}