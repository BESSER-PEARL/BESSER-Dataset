





import java.util.List;
import java.util.ArrayList;

public class analysis_trace_ComparedAction  {

    private String dSteps;
    private String dOutgoings;
    private boolean found;
    private String dIncomings;





    private trace_analysis_Action trace_analysis_action;


    public analysis_trace_ComparedAction(
        String dSteps,        String dOutgoings,        boolean found,        String dIncomings    ) {
        this.dSteps = dSteps;
        this.dOutgoings = dOutgoings;
        this.found = found;
        this.dIncomings = dIncomings;
    }


    public String getDsteps() {
        return dSteps;
    }

    public void setDsteps(String dSteps) {
        this.dSteps = dSteps;
    }
    public String getDoutgoings() {
        return dOutgoings;
    }

    public void setDoutgoings(String dOutgoings) {
        this.dOutgoings = dOutgoings;
    }
    public boolean getFound() {
        return found;
    }

    public void setFound(boolean found) {
        this.found = found;
    }
    public String getDincomings() {
        return dIncomings;
    }

    public void setDincomings(String dIncomings) {
        this.dIncomings = dIncomings;
    }

    public trace_analysis_Action getTrace_analysis_action() {
        return trace_analysis_action;
    }

    public void setTrace_analysis_action(trace_analysis_Action trace_analysis_action) {
        this.trace_analysis_action = trace_analysis_action;
    }

}