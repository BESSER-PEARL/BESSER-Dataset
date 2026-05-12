





import java.util.List;
import java.util.ArrayList;

public class MDAIntermediateStateMachine_State  {

    private String name;





    private MDAIntermediateStateMachine_Content mdaintermediatestatemachine_content;


    public MDAIntermediateStateMachine_State(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MDAIntermediateStateMachine_Content getMdaintermediatestatemachine_content() {
        return mdaintermediatestatemachine_content;
    }

    public void setMdaintermediatestatemachine_content(MDAIntermediateStateMachine_Content mdaintermediatestatemachine_content) {
        this.mdaintermediatestatemachine_content = mdaintermediatestatemachine_content;
    }

}