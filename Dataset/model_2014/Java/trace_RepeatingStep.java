





import java.util.List;
import java.util.ArrayList;

public class trace_RepeatingStep extends StepSpec {






    private trace_RepeatingStep trace_repeatingstep;




    private trace_StepPattern trace_steppattern;




    private List<trace_RepeatingStep> trace_repeatingsteps;


    public trace_RepeatingStep(
    ) {
        super(
        );
        this.trace_repeatingsteps = new ArrayList<>();
    }

    public trace_RepeatingStep(
        ArrayList<trace_RepeatingStep> trace_repeatingsteps    ) {
        this.trace_repeatingsteps = trace_repeatingsteps;
    }


    public trace_RepeatingStep getTrace_repeatingstep() {
        return trace_repeatingstep;
    }

    public void setTrace_repeatingstep(trace_RepeatingStep trace_repeatingstep) {
        this.trace_repeatingstep = trace_repeatingstep;
    }
    public trace_StepPattern getTrace_steppattern() {
        return trace_steppattern;
    }

    public void setTrace_steppattern(trace_StepPattern trace_steppattern) {
        this.trace_steppattern = trace_steppattern;
    }
    public List<trace_RepeatingStep> getTrace_repeatingsteps() {
        return trace_repeatingsteps;
    }

    public void addTrace_repeatingstep(Trace_repeatingstep trace_repeatingstep) {
        this.trace_repeatingsteps.add(trace_repeatingstep);
    }

}