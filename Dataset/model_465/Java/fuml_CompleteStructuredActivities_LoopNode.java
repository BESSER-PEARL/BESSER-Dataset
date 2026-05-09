





import java.util.List;
import java.util.ArrayList;

public class fuml_CompleteStructuredActivities_LoopNode extends StructuredActivityNode {

    private boolean testedFirst;





    private List<BasicActions_InputPin> basicactions_inputpins;


    public fuml_CompleteStructuredActivities_LoopNode(
        boolean testedFirst    ) {
        super(
        );
        this.testedFirst = testedFirst;
        this.basicactions_inputpins = new ArrayList<>();
    }

    public fuml_CompleteStructuredActivities_LoopNode(
        boolean testedFirst        ArrayList<BasicActions_InputPin> basicactions_inputpins    ) {
        this.testedFirst = testedFirst;
        this.basicactions_inputpins = basicactions_inputpins;
    }

    public boolean getTestedfirst() {
        return testedFirst;
    }

    public void setTestedfirst(boolean testedFirst) {
        this.testedFirst = testedFirst;
    }

    public List<BasicActions_InputPin> getBasicactions_inputpins() {
        return basicactions_inputpins;
    }

    public void addBasicactions_inputpin(Basicactions_inputpin basicactions_inputpin) {
        this.basicactions_inputpins.add(basicactions_inputpin);
    }

}