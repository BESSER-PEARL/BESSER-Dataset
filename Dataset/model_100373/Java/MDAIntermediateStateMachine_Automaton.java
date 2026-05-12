





import java.util.List;
import java.util.ArrayList;

public class MDAIntermediateStateMachine_Automaton  {

    private String name;





    private MDAIntermediateStateMachine_State mdaintermediatestatemachine_state;




    private MDAIntermediateStateMachine_Content mdaintermediatestatemachine_content;




    private List<MDAIntermediateStateMachine_State> mdaintermediatestatemachine_states;


    public MDAIntermediateStateMachine_Automaton(
        String name    ) {
        this.name = name;
        this.mdaintermediatestatemachine_states = new ArrayList<>();
    }

    public MDAIntermediateStateMachine_Automaton(
        String name        ArrayList<MDAIntermediateStateMachine_State> mdaintermediatestatemachine_states    ) {
        this.name = name;
        this.mdaintermediatestatemachine_states = mdaintermediatestatemachine_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MDAIntermediateStateMachine_State getMdaintermediatestatemachine_state() {
        return mdaintermediatestatemachine_state;
    }

    public void setMdaintermediatestatemachine_state(MDAIntermediateStateMachine_State mdaintermediatestatemachine_state) {
        this.mdaintermediatestatemachine_state = mdaintermediatestatemachine_state;
    }
    public MDAIntermediateStateMachine_Content getMdaintermediatestatemachine_content() {
        return mdaintermediatestatemachine_content;
    }

    public void setMdaintermediatestatemachine_content(MDAIntermediateStateMachine_Content mdaintermediatestatemachine_content) {
        this.mdaintermediatestatemachine_content = mdaintermediatestatemachine_content;
    }
    public List<MDAIntermediateStateMachine_State> getMdaintermediatestatemachine_states() {
        return mdaintermediatestatemachine_states;
    }

    public void addMdaintermediatestatemachine_state(Mdaintermediatestatemachine_state mdaintermediatestatemachine_state) {
        this.mdaintermediatestatemachine_states.add(mdaintermediatestatemachine_state);
    }

}