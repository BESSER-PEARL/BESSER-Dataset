





import java.util.List;
import java.util.ArrayList;

public class iec61131_interfaces_Input_Declarations extends Io_Var_Declaration {

    private boolean retain;



    public iec61131_interfaces_Input_Declarations(
        boolean retain    ) {
        super(
        );
        this.retain = retain;
    }


    public boolean getRetain() {
        return retain;
    }

    public void setRetain(boolean retain) {
        this.retain = retain;
    }


}