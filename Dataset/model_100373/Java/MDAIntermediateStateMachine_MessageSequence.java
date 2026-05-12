





import java.util.List;
import java.util.ArrayList;

public class MDAIntermediateStateMachine_MessageSequence  {






    private MDAIntermediateStateMachine_State mdaintermediatestatemachine_state;




    private List<MDAIntermediateStateMachine_Message> mdaintermediatestatemachine_messages;


    public MDAIntermediateStateMachine_MessageSequence(
    ) {
        this.mdaintermediatestatemachine_messages = new ArrayList<>();
    }

    public MDAIntermediateStateMachine_MessageSequence(
        ArrayList<MDAIntermediateStateMachine_Message> mdaintermediatestatemachine_messages    ) {
        this.mdaintermediatestatemachine_messages = mdaintermediatestatemachine_messages;
    }


    public MDAIntermediateStateMachine_State getMdaintermediatestatemachine_state() {
        return mdaintermediatestatemachine_state;
    }

    public void setMdaintermediatestatemachine_state(MDAIntermediateStateMachine_State mdaintermediatestatemachine_state) {
        this.mdaintermediatestatemachine_state = mdaintermediatestatemachine_state;
    }
    public List<MDAIntermediateStateMachine_Message> getMdaintermediatestatemachine_messages() {
        return mdaintermediatestatemachine_messages;
    }

    public void addMdaintermediatestatemachine_message(Mdaintermediatestatemachine_message mdaintermediatestatemachine_message) {
        this.mdaintermediatestatemachine_messages.add(mdaintermediatestatemachine_message);
    }

}