





import java.util.List;
import java.util.ArrayList;

public class analysis_scheduling_FSM extends ActorSelectionSchedule {

    private String terminalState;
    private String startState;



    public analysis_scheduling_FSM(
        String terminalState,        String startState    ) {
        super(
        );
        this.terminalState = terminalState;
        this.startState = startState;
    }


    public String getTerminalstate() {
        return terminalState;
    }

    public void setTerminalstate(String terminalState) {
        this.terminalState = terminalState;
    }
    public String getStartstate() {
        return startState;
    }

    public void setStartstate(String startState) {
        this.startState = startState;
    }


}