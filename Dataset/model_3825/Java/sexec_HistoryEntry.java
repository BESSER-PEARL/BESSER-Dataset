





import java.util.List;
import java.util.ArrayList;

public class sexec_HistoryEntry extends Step {

    private boolean deep;





    private sexec_Step sexec_step;




    private sexec_Step sexec_step;




    private sexec_ExecutionRegion sexec_executionregion;


    public sexec_HistoryEntry(
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

    public sexec_Step getSexec_step() {
        return sexec_step;
    }

    public void setSexec_step(sexec_Step sexec_step) {
        this.sexec_step = sexec_step;
    }
    public sexec_Step getSexec_step() {
        return sexec_step;
    }

    public void setSexec_step(sexec_Step sexec_step) {
        this.sexec_step = sexec_step;
    }
    public sexec_ExecutionRegion getSexec_executionregion() {
        return sexec_executionregion;
    }

    public void setSexec_executionregion(sexec_ExecutionRegion sexec_executionregion) {
        this.sexec_executionregion = sexec_executionregion;
    }

}