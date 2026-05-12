





import java.util.List;
import java.util.ArrayList;

public class MDAIntermediateStateMachine_Participant  {

    private String name;





    private MDAIntermediateStateMachine_Automaton mdaintermediatestatemachine_automaton;




    private MDAIntermediateStateMachine_Content mdaintermediatestatemachine_content;


    public MDAIntermediateStateMachine_Participant(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MDAIntermediateStateMachine_Automaton getMdaintermediatestatemachine_automaton() {
        return mdaintermediatestatemachine_automaton;
    }

    public void setMdaintermediatestatemachine_automaton(MDAIntermediateStateMachine_Automaton mdaintermediatestatemachine_automaton) {
        this.mdaintermediatestatemachine_automaton = mdaintermediatestatemachine_automaton;
    }
    public MDAIntermediateStateMachine_Content getMdaintermediatestatemachine_content() {
        return mdaintermediatestatemachine_content;
    }

    public void setMdaintermediatestatemachine_content(MDAIntermediateStateMachine_Content mdaintermediatestatemachine_content) {
        this.mdaintermediatestatemachine_content = mdaintermediatestatemachine_content;
    }

}