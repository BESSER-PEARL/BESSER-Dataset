





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_AcceptEventAction extends Action {

    private boolean isUnmarshall;





    private List<CompleteDSLPckg_OutputPin> completedslpckg_outputpins;




    private List<CompleteDSLPckg_Trigger> completedslpckg_triggers;


    public CompleteDSLPckg_AcceptEventAction(
        boolean isUnmarshall    ) {
        super(
        );
        this.isUnmarshall = isUnmarshall;
        this.completedslpckg_outputpins = new ArrayList<>();
        this.completedslpckg_triggers = new ArrayList<>();
    }

    public CompleteDSLPckg_AcceptEventAction(
        boolean isUnmarshall        ArrayList<CompleteDSLPckg_OutputPin> completedslpckg_outputpins,        ArrayList<CompleteDSLPckg_Trigger> completedslpckg_triggers    ) {
        this.isUnmarshall = isUnmarshall;
        this.completedslpckg_outputpins = completedslpckg_outputpins;
        this.completedslpckg_triggers = completedslpckg_triggers;
    }

    public boolean getIsunmarshall() {
        return isUnmarshall;
    }

    public void setIsunmarshall(boolean isUnmarshall) {
        this.isUnmarshall = isUnmarshall;
    }

    public List<CompleteDSLPckg_OutputPin> getCompletedslpckg_outputpins() {
        return completedslpckg_outputpins;
    }

    public void addCompletedslpckg_outputpin(Completedslpckg_outputpin completedslpckg_outputpin) {
        this.completedslpckg_outputpins.add(completedslpckg_outputpin);
    }
    public List<CompleteDSLPckg_Trigger> getCompletedslpckg_triggers() {
        return completedslpckg_triggers;
    }

    public void addCompletedslpckg_trigger(Completedslpckg_trigger completedslpckg_trigger) {
        this.completedslpckg_triggers.add(completedslpckg_trigger);
    }

}