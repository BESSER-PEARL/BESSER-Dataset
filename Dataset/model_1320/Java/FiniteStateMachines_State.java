





import java.util.List;
import java.util.ArrayList;

public class FiniteStateMachines_State  {

    private boolean isStartState;
    private boolean isEndState;
    private String name;





    private FiniteStateMachines_FiniteStateMachine finitestatemachines_finitestatemachine;


    public FiniteStateMachines_State(
        boolean isStartState,        boolean isEndState,        String name    ) {
        this.isStartState = isStartState;
        this.isEndState = isEndState;
        this.name = name;
    }


    public boolean getIsstartstate() {
        return isStartState;
    }

    public void setIsstartstate(boolean isStartState) {
        this.isStartState = isStartState;
    }
    public boolean getIsendstate() {
        return isEndState;
    }

    public void setIsendstate(boolean isEndState) {
        this.isEndState = isEndState;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public FiniteStateMachines_FiniteStateMachine getFinitestatemachines_finitestatemachine() {
        return finitestatemachines_finitestatemachine;
    }

    public void setFinitestatemachines_finitestatemachine(FiniteStateMachines_FiniteStateMachine finitestatemachines_finitestatemachine) {
        this.finitestatemachines_finitestatemachine = finitestatemachines_finitestatemachine;
    }

}