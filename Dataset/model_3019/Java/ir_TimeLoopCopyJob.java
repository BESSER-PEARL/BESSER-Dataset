





import java.util.List;
import java.util.ArrayList;

public class ir_TimeLoopCopyJob extends Job {






    private List<ir_TimeLoopCopy> ir_timeloopcopys;




    private ir_TimeLoop ir_timeloop;


    public ir_TimeLoopCopyJob(
    ) {
        super(
        );
        this.ir_timeloopcopys = new ArrayList<>();
    }

    public ir_TimeLoopCopyJob(
        ArrayList<ir_TimeLoopCopy> ir_timeloopcopys    ) {
        this.ir_timeloopcopys = ir_timeloopcopys;
    }


    public List<ir_TimeLoopCopy> getIr_timeloopcopys() {
        return ir_timeloopcopys;
    }

    public void addIr_timeloopcopy(Ir_timeloopcopy ir_timeloopcopy) {
        this.ir_timeloopcopys.add(ir_timeloopcopy);
    }
    public ir_TimeLoop getIr_timeloop() {
        return ir_timeloop;
    }

    public void setIr_timeloop(ir_TimeLoop ir_timeloop) {
        this.ir_timeloop = ir_timeloop;
    }

}