





import java.util.List;
import java.util.ArrayList;

public class gast_accesses_VariableAccess extends Access {

    private boolean write;





    private Variable variable;


    public gast_accesses_VariableAccess(
        boolean write    ) {
        super(
        );
        this.write = write;
    }


    public boolean getWrite() {
        return write;
    }

    public void setWrite(boolean write) {
        this.write = write;
    }

    public Variable getVariable() {
        return variable;
    }

    public void setVariable(Variable variable) {
        this.variable = variable;
    }

}