





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_UnmarshallAction extends Action {






    private CompleteDSLPckg_Classifier completedslpckg_classifier;




    private List<CompleteDSLPckg_OutputPin> completedslpckg_outputpins;




    private CompleteDSLPckg_InputPin completedslpckg_inputpin;


    public CompleteDSLPckg_UnmarshallAction(
    ) {
        super(
        );
        this.completedslpckg_outputpins = new ArrayList<>();
    }

    public CompleteDSLPckg_UnmarshallAction(
        ArrayList<CompleteDSLPckg_OutputPin> completedslpckg_outputpins    ) {
        this.completedslpckg_outputpins = completedslpckg_outputpins;
    }


    public CompleteDSLPckg_Classifier getCompletedslpckg_classifier() {
        return completedslpckg_classifier;
    }

    public void setCompletedslpckg_classifier(CompleteDSLPckg_Classifier completedslpckg_classifier) {
        this.completedslpckg_classifier = completedslpckg_classifier;
    }
    public List<CompleteDSLPckg_OutputPin> getCompletedslpckg_outputpins() {
        return completedslpckg_outputpins;
    }

    public void addCompletedslpckg_outputpin(Completedslpckg_outputpin completedslpckg_outputpin) {
        this.completedslpckg_outputpins.add(completedslpckg_outputpin);
    }
    public CompleteDSLPckg_InputPin getCompletedslpckg_inputpin() {
        return completedslpckg_inputpin;
    }

    public void setCompletedslpckg_inputpin(CompleteDSLPckg_InputPin completedslpckg_inputpin) {
        this.completedslpckg_inputpin = completedslpckg_inputpin;
    }

}