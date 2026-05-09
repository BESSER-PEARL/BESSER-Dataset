





import java.util.List;
import java.util.ArrayList;

public class analysis_scheduling_FSMCombination  {

    private String combinator;





    private FSMCondition fsmcondition;


    public analysis_scheduling_FSMCombination(
        String combinator    ) {
        this.combinator = combinator;
    }


    public String getCombinator() {
        return combinator;
    }

    public void setCombinator(String combinator) {
        this.combinator = combinator;
    }

    public FSMCondition getFsmcondition() {
        return fsmcondition;
    }

    public void setFsmcondition(FSMCondition fsmcondition) {
        this.fsmcondition = fsmcondition;
    }

}