





import java.util.List;
import java.util.ArrayList;

public class fuml_BasicActions_Action extends ExecutableNode {

    private boolean locallyReentrant;





    private Kernel_Classifier kernel_classifier;




    private List<BasicActions_OutputPin> basicactions_outputpins;




    private List<BasicActions_InputPin> basicactions_inputpins;


    public fuml_BasicActions_Action(
        boolean locallyReentrant    ) {
        super(
        );
        this.locallyReentrant = locallyReentrant;
        this.basicactions_outputpins = new ArrayList<>();
        this.basicactions_inputpins = new ArrayList<>();
    }

    public fuml_BasicActions_Action(
        boolean locallyReentrant        ArrayList<BasicActions_OutputPin> basicactions_outputpins,        ArrayList<BasicActions_InputPin> basicactions_inputpins    ) {
        this.locallyReentrant = locallyReentrant;
        this.basicactions_outputpins = basicactions_outputpins;
        this.basicactions_inputpins = basicactions_inputpins;
    }

    public boolean getLocallyreentrant() {
        return locallyReentrant;
    }

    public void setLocallyreentrant(boolean locallyReentrant) {
        this.locallyReentrant = locallyReentrant;
    }

    public Kernel_Classifier getKernel_classifier() {
        return kernel_classifier;
    }

    public void setKernel_classifier(Kernel_Classifier kernel_classifier) {
        this.kernel_classifier = kernel_classifier;
    }
    public List<BasicActions_OutputPin> getBasicactions_outputpins() {
        return basicactions_outputpins;
    }

    public void addBasicactions_outputpin(Basicactions_outputpin basicactions_outputpin) {
        this.basicactions_outputpins.add(basicactions_outputpin);
    }
    public List<BasicActions_InputPin> getBasicactions_inputpins() {
        return basicactions_inputpins;
    }

    public void addBasicactions_inputpin(Basicactions_inputpin basicactions_inputpin) {
        this.basicactions_inputpins.add(basicactions_inputpin);
    }

}