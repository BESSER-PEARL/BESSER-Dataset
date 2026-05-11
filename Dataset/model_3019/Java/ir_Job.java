





import java.util.List;
import java.util.ArrayList;

public class ir_Job extends IrAnnotable {

    private boolean onCycle;
    private float at;
    private String name;





    private ir_JobContainer ir_jobcontainer;




    private ir_JobContainer ir_jobcontainer;


    public ir_Job(
        boolean onCycle,        float at,        String name    ) {
        super(
        );
        this.onCycle = onCycle;
        this.at = at;
        this.name = name;
    }


    public boolean getOncycle() {
        return onCycle;
    }

    public void setOncycle(boolean onCycle) {
        this.onCycle = onCycle;
    }
    public float getAt() {
        return at;
    }

    public void setAt(float at) {
        this.at = at;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ir_JobContainer getIr_jobcontainer() {
        return ir_jobcontainer;
    }

    public void setIr_jobcontainer(ir_JobContainer ir_jobcontainer) {
        this.ir_jobcontainer = ir_jobcontainer;
    }
    public ir_JobContainer getIr_jobcontainer() {
        return ir_jobcontainer;
    }

    public void setIr_jobcontainer(ir_JobContainer ir_jobcontainer) {
        this.ir_jobcontainer = ir_jobcontainer;
    }

}