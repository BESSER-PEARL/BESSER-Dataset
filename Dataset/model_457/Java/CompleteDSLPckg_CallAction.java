





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_CallAction extends InvocationAction {

    private boolean isSynchronous;





    private List<CompleteDSLPckg_OutputPin> completedslpckg_outputpins;


    public CompleteDSLPckg_CallAction(
        boolean isSynchronous    ) {
        super(
        );
        this.isSynchronous = isSynchronous;
        this.completedslpckg_outputpins = new ArrayList<>();
    }

    public CompleteDSLPckg_CallAction(
        boolean isSynchronous        ArrayList<CompleteDSLPckg_OutputPin> completedslpckg_outputpins    ) {
        this.isSynchronous = isSynchronous;
        this.completedslpckg_outputpins = completedslpckg_outputpins;
    }

    public boolean getIssynchronous() {
        return isSynchronous;
    }

    public void setIssynchronous(boolean isSynchronous) {
        this.isSynchronous = isSynchronous;
    }

    public List<CompleteDSLPckg_OutputPin> getCompletedslpckg_outputpins() {
        return completedslpckg_outputpins;
    }

    public void addCompletedslpckg_outputpin(Completedslpckg_outputpin completedslpckg_outputpin) {
        this.completedslpckg_outputpins.add(completedslpckg_outputpin);
    }

}