





import java.util.List;
import java.util.ArrayList;

public class analysis_trace_MarkovModelActionData  {

    private boolean first;
    private String successors;





    private trace_analysis_Action trace_analysis_action;




    private List<ActionToLongMap> actiontolongmaps;


    public analysis_trace_MarkovModelActionData(
        boolean first,        String successors    ) {
        this.first = first;
        this.successors = successors;
        this.actiontolongmaps = new ArrayList<>();
    }

    public analysis_trace_MarkovModelActionData(
        boolean first,        String successors        ArrayList<ActionToLongMap> actiontolongmaps    ) {
        this.first = first;
        this.successors = successors;
        this.actiontolongmaps = actiontolongmaps;
    }

    public boolean getFirst() {
        return first;
    }

    public void setFirst(boolean first) {
        this.first = first;
    }
    public String getSuccessors() {
        return successors;
    }

    public void setSuccessors(String successors) {
        this.successors = successors;
    }

    public trace_analysis_Action getTrace_analysis_action() {
        return trace_analysis_action;
    }

    public void setTrace_analysis_action(trace_analysis_Action trace_analysis_action) {
        this.trace_analysis_action = trace_analysis_action;
    }
    public List<ActionToLongMap> getActiontolongmaps() {
        return actiontolongmaps;
    }

    public void addActiontolongmap(Actiontolongmap actiontolongmap) {
        this.actiontolongmaps.add(actiontolongmap);
    }

}