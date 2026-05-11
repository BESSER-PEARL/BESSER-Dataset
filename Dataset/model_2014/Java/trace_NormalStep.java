





import java.util.List;
import java.util.ArrayList;

public class trace_NormalStep extends StepSpec, Step {






    private trace_Step trace_step;




    private List<trace_Step> trace_steps;


    public trace_NormalStep(
    ) {
        super(
        );
        this.trace_steps = new ArrayList<>();
    }

    public trace_NormalStep(
        ArrayList<trace_Step> trace_steps    ) {
        this.trace_steps = trace_steps;
    }


    public trace_Step getTrace_step() {
        return trace_step;
    }

    public void setTrace_step(trace_Step trace_step) {
        this.trace_step = trace_step;
    }
    public List<trace_Step> getTrace_steps() {
        return trace_steps;
    }

    public void addTrace_step(Trace_step trace_step) {
        this.trace_steps.add(trace_step);
    }

}