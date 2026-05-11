





import java.util.List;
import java.util.ArrayList;

public class sexec_SaveHistory extends Step {

    private boolean deep;





    private sexec_ExecutionRegion sexec_executionregion;


    public sexec_SaveHistory(
        boolean deep    ) {
        super(
        );
        this.deep = deep;
    }


    public boolean getDeep() {
        return deep;
    }

    public void setDeep(boolean deep) {
        this.deep = deep;
    }

    public sexec_ExecutionRegion getSexec_executionregion() {
        return sexec_executionregion;
    }

    public void setSexec_executionregion(sexec_ExecutionRegion sexec_executionregion) {
        this.sexec_executionregion = sexec_executionregion;
    }

}