





import java.util.List;
import java.util.ArrayList;

public class junitmodel_JUnitProblem extends TestProblem {

    private boolean lastTraceWasFiltered;



    public junitmodel_JUnitProblem(
        boolean lastTraceWasFiltered    ) {
        super(
        );
        this.lastTraceWasFiltered = lastTraceWasFiltered;
    }


    public boolean getLasttracewasfiltered() {
        return lastTraceWasFiltered;
    }

    public void setLasttracewasfiltered(boolean lastTraceWasFiltered) {
        this.lastTraceWasFiltered = lastTraceWasFiltered;
    }


}