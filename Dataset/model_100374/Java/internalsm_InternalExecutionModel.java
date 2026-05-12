





import java.util.List;
import java.util.ArrayList;

public class internalsm_InternalExecutionModel  {

    private String context;





    private internalsm_Event internalsm_event;




    private List<internalsm_EventToken> internalsm_eventtokens;




    private List<internalsm_StateMachine> internalsm_statemachines;


    public internalsm_InternalExecutionModel(
        String context    ) {
        this.context = context;
        this.internalsm_eventtokens = new ArrayList<>();
        this.internalsm_statemachines = new ArrayList<>();
    }

    public internalsm_InternalExecutionModel(
        String context        ArrayList<internalsm_EventToken> internalsm_eventtokens,        ArrayList<internalsm_StateMachine> internalsm_statemachines    ) {
        this.context = context;
        this.internalsm_eventtokens = internalsm_eventtokens;
        this.internalsm_statemachines = internalsm_statemachines;
    }

    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }

    public internalsm_Event getInternalsm_event() {
        return internalsm_event;
    }

    public void setInternalsm_event(internalsm_Event internalsm_event) {
        this.internalsm_event = internalsm_event;
    }
    public List<internalsm_EventToken> getInternalsm_eventtokens() {
        return internalsm_eventtokens;
    }

    public void addInternalsm_eventtoken(Internalsm_eventtoken internalsm_eventtoken) {
        this.internalsm_eventtokens.add(internalsm_eventtoken);
    }
    public List<internalsm_StateMachine> getInternalsm_statemachines() {
        return internalsm_statemachines;
    }

    public void addInternalsm_statemachine(Internalsm_statemachine internalsm_statemachine) {
        this.internalsm_statemachines.add(internalsm_statemachine);
    }

}