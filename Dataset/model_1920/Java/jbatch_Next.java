





import java.util.List;
import java.util.ArrayList;

public class jbatch_Next  {

    private String to;
    private String on;





    private jbatch_Flow jbatch_flow;




    private jbatch_Step jbatch_step;


    public jbatch_Next(
        String to,        String on    ) {
        this.to = to;
        this.on = on;
    }


    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getOn() {
        return on;
    }

    public void setOn(String on) {
        this.on = on;
    }

    public jbatch_Flow getJbatch_flow() {
        return jbatch_flow;
    }

    public void setJbatch_flow(jbatch_Flow jbatch_flow) {
        this.jbatch_flow = jbatch_flow;
    }
    public jbatch_Step getJbatch_step() {
        return jbatch_step;
    }

    public void setJbatch_step(jbatch_Step jbatch_step) {
        this.jbatch_step = jbatch_step;
    }

}