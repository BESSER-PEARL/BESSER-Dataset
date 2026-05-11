





import java.util.List;
import java.util.ArrayList;

public class sexec_StateSwitch extends Step {

    private int stateConfigurationIdx;





    private sexec_ExecutionRegion sexec_executionregion;


    public sexec_StateSwitch(
        int stateConfigurationIdx    ) {
        super(
        );
        this.stateConfigurationIdx = stateConfigurationIdx;
    }


    public int getStateconfigurationidx() {
        return stateConfigurationIdx;
    }

    public void setStateconfigurationidx(int stateConfigurationIdx) {
        this.stateConfigurationIdx = stateConfigurationIdx;
    }

    public sexec_ExecutionRegion getSexec_executionregion() {
        return sexec_executionregion;
    }

    public void setSexec_executionregion(sexec_ExecutionRegion sexec_executionregion) {
        this.sexec_executionregion = sexec_executionregion;
    }

}