





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ReplyAction extends Action {






    private List<CompleteDSLPckg_InputPin> completedslpckg_inputpins;




    private CompleteDSLPckg_InputPin completedslpckg_inputpin;




    private CompleteDSLPckg_Trigger completedslpckg_trigger;


    public CompleteDSLPckg_ReplyAction(
    ) {
        super(
        );
        this.completedslpckg_inputpins = new ArrayList<>();
    }

    public CompleteDSLPckg_ReplyAction(
        ArrayList<CompleteDSLPckg_InputPin> completedslpckg_inputpins    ) {
        this.completedslpckg_inputpins = completedslpckg_inputpins;
    }


    public List<CompleteDSLPckg_InputPin> getCompletedslpckg_inputpins() {
        return completedslpckg_inputpins;
    }

    public void addCompletedslpckg_inputpin(Completedslpckg_inputpin completedslpckg_inputpin) {
        this.completedslpckg_inputpins.add(completedslpckg_inputpin);
    }
    public CompleteDSLPckg_InputPin getCompletedslpckg_inputpin() {
        return completedslpckg_inputpin;
    }

    public void setCompletedslpckg_inputpin(CompleteDSLPckg_InputPin completedslpckg_inputpin) {
        this.completedslpckg_inputpin = completedslpckg_inputpin;
    }
    public CompleteDSLPckg_Trigger getCompletedslpckg_trigger() {
        return completedslpckg_trigger;
    }

    public void setCompletedslpckg_trigger(CompleteDSLPckg_Trigger completedslpckg_trigger) {
        this.completedslpckg_trigger = completedslpckg_trigger;
    }

}