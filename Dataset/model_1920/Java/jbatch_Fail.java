





import java.util.List;
import java.util.ArrayList;

public class jbatch_Fail  {

    private String exitStatus;
    private String on;





    private jbatch_Step jbatch_step;




    private jbatch_Flow jbatch_flow;


    public jbatch_Fail(
        String exitStatus,        String on    ) {
        this.exitStatus = exitStatus;
        this.on = on;
    }


    public String getExitstatus() {
        return exitStatus;
    }

    public void setExitstatus(String exitStatus) {
        this.exitStatus = exitStatus;
    }
    public String getOn() {
        return on;
    }

    public void setOn(String on) {
        this.on = on;
    }

    public jbatch_Step getJbatch_step() {
        return jbatch_step;
    }

    public void setJbatch_step(jbatch_Step jbatch_step) {
        this.jbatch_step = jbatch_step;
    }
    public jbatch_Flow getJbatch_flow() {
        return jbatch_flow;
    }

    public void setJbatch_flow(jbatch_Flow jbatch_flow) {
        this.jbatch_flow = jbatch_flow;
    }

}