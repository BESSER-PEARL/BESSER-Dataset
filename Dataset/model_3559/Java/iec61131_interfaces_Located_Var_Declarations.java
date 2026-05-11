





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_Located_Var_Declarations extends Program_Vars {

    private boolean retain;
    private boolean constant;



    public iec61131_interfaces_Located_Var_Declarations(
        boolean retain,        boolean constant    ) {
        super(
        );
        this.retain = retain;
        this.constant = constant;
    }


    public boolean getRetain() {
        return retain;
    }

    public void setRetain(boolean retain) {
        this.retain = retain;
    }
    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }


}