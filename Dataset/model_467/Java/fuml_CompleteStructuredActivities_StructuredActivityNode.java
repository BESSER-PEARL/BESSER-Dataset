





import java.util.List;
import java.util.ArrayList;

public class fuml_CompleteStructuredActivities_StructuredActivityNode extends Action {

    private boolean mustIsolate;





    private List<BasicActions_InputPin> basicactions_inputpins;




    private List<BasicActions_OutputPin> basicactions_outputpins;


    public fuml_CompleteStructuredActivities_StructuredActivityNode(
        boolean mustIsolate    ) {
        super(
        );
        this.mustIsolate = mustIsolate;
        this.basicactions_inputpins = new ArrayList<>();
        this.basicactions_outputpins = new ArrayList<>();
    }

    public fuml_CompleteStructuredActivities_StructuredActivityNode(
        boolean mustIsolate        ArrayList<BasicActions_InputPin> basicactions_inputpins,        ArrayList<BasicActions_OutputPin> basicactions_outputpins    ) {
        this.mustIsolate = mustIsolate;
        this.basicactions_inputpins = basicactions_inputpins;
        this.basicactions_outputpins = basicactions_outputpins;
    }

    public boolean getMustisolate() {
        return mustIsolate;
    }

    public void setMustisolate(boolean mustIsolate) {
        this.mustIsolate = mustIsolate;
    }

    public List<BasicActions_InputPin> getBasicactions_inputpins() {
        return basicactions_inputpins;
    }

    public void addBasicactions_inputpin(Basicactions_inputpin basicactions_inputpin) {
        this.basicactions_inputpins.add(basicactions_inputpin);
    }
    public List<BasicActions_OutputPin> getBasicactions_outputpins() {
        return basicactions_outputpins;
    }

    public void addBasicactions_outputpin(Basicactions_outputpin basicactions_outputpin) {
        this.basicactions_outputpins.add(basicactions_outputpin);
    }

}