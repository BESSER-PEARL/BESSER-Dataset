





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_External_Var_Declarations extends Other_Var_Declaration {

    private boolean constant;



    public iec61131_interfaces_External_Var_Declarations(
        boolean constant    ) {
        super(
        );
        this.constant = constant;
    }


    public boolean getConstant() {
        return constant;
    }

    public void setConstant(boolean constant) {
        this.constant = constant;
    }


}