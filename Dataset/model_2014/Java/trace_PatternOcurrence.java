





import java.util.List;
import java.util.ArrayList;

public class trace_PatternOcurrence extends Step {

    private int repet;





    private trace_StepPattern trace_steppattern;


    public trace_PatternOcurrence(
        int repet    ) {
        super(
        );
        this.repet = repet;
    }


    public int getRepet() {
        return repet;
    }

    public void setRepet(int repet) {
        this.repet = repet;
    }

    public trace_StepPattern getTrace_steppattern() {
        return trace_steppattern;
    }

    public void setTrace_steppattern(trace_StepPattern trace_steppattern) {
        this.trace_steppattern = trace_steppattern;
    }

}