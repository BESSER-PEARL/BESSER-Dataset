





import java.util.List;
import java.util.ArrayList;

public class internalsm_StateMachine  {

    private String context;
    private int priority;





    private List<internalsm_State> internalsm_states;


    public internalsm_StateMachine(
        String context,        int priority    ) {
        this.context = context;
        this.priority = priority;
        this.internalsm_states = new ArrayList<>();
    }

    public internalsm_StateMachine(
        String context,        int priority        ArrayList<internalsm_State> internalsm_states    ) {
        this.context = context;
        this.priority = priority;
        this.internalsm_states = internalsm_states;
    }

    public String getContext() {
        return context;
    }

    public void setContext(String context) {
        this.context = context;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }

    public List<internalsm_State> getInternalsm_states() {
        return internalsm_states;
    }

    public void addInternalsm_state(Internalsm_state internalsm_state) {
        this.internalsm_states.add(internalsm_state);
    }

}