





import java.util.List;
import java.util.ArrayList;

public class minioclcs_MultiplicityCS extends CSTrace {

    private boolean upperMult;
    private int mandatory;
    private boolean opt;
    private int upperInt;
    private boolean mult;
    private int lowerInt;



    public minioclcs_MultiplicityCS(
        boolean upperMult,        int mandatory,        boolean opt,        int upperInt,        boolean mult,        int lowerInt    ) {
        super(
        );
        this.upperMult = upperMult;
        this.mandatory = mandatory;
        this.opt = opt;
        this.upperInt = upperInt;
        this.mult = mult;
        this.lowerInt = lowerInt;
    }


    public boolean getUppermult() {
        return upperMult;
    }

    public void setUppermult(boolean upperMult) {
        this.upperMult = upperMult;
    }
    public int getMandatory() {
        return mandatory;
    }

    public void setMandatory(int mandatory) {
        this.mandatory = mandatory;
    }
    public boolean getOpt() {
        return opt;
    }

    public void setOpt(boolean opt) {
        this.opt = opt;
    }
    public int getUpperint() {
        return upperInt;
    }

    public void setUpperint(int upperInt) {
        this.upperInt = upperInt;
    }
    public boolean getMult() {
        return mult;
    }

    public void setMult(boolean mult) {
        this.mult = mult;
    }
    public int getLowerint() {
        return lowerInt;
    }

    public void setLowerint(int lowerInt) {
        this.lowerInt = lowerInt;
    }


}