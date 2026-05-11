





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_Global_Var_Declarations extends Library_Element_Declaration {

    private boolean constant;
    private boolean retain;



    public iec61131_interfaces_Global_Var_Declarations(
        boolean constant,        boolean retain    ) {
        super(
        );
        this.constant = constant;
        this.retain = retain;
    }


    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }
    public boolean getRetain() {
        return retain;
    }

    public void setRetain(boolean retain) {
        this.retain = retain;
    }


}