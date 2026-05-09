





import java.util.List;
import java.util.ArrayList;

public class fuml_CompleteStructuredActivities_Clause extends Element {






    private List<CompleteStructuredActivities_ExecutableNode> completestructuredactivities_executablenodes;




    private List<BasicActions_OutputPin> basicactions_outputpins;




    private List<CompleteStructuredActivities_ExecutableNode> completestructuredactivities_executablenodes;




    private BasicActions_OutputPin basicactions_outputpin;


    public fuml_CompleteStructuredActivities_Clause(
    ) {
        super(
        );
        this.completestructuredactivities_executablenodes = new ArrayList<>();
        this.basicactions_outputpins = new ArrayList<>();
        this.completestructuredactivities_executablenodes = new ArrayList<>();
    }

    public fuml_CompleteStructuredActivities_Clause(
        ArrayList<CompleteStructuredActivities_ExecutableNode> completestructuredactivities_executablenodes,        ArrayList<BasicActions_OutputPin> basicactions_outputpins,        ArrayList<CompleteStructuredActivities_ExecutableNode> completestructuredactivities_executablenodes    ) {
        this.completestructuredactivities_executablenodes = completestructuredactivities_executablenodes;
        this.basicactions_outputpins = basicactions_outputpins;
        this.completestructuredactivities_executablenodes = completestructuredactivities_executablenodes;
    }


    public List<CompleteStructuredActivities_ExecutableNode> getCompletestructuredactivities_executablenodes() {
        return completestructuredactivities_executablenodes;
    }

    public void addCompletestructuredactivities_executablenode(Completestructuredactivities_executablenode completestructuredactivities_executablenode) {
        this.completestructuredactivities_executablenodes.add(completestructuredactivities_executablenode);
    }
    public List<BasicActions_OutputPin> getBasicactions_outputpins() {
        return basicactions_outputpins;
    }

    public void addBasicactions_outputpin(Basicactions_outputpin basicactions_outputpin) {
        this.basicactions_outputpins.add(basicactions_outputpin);
    }
    public List<CompleteStructuredActivities_ExecutableNode> getCompletestructuredactivities_executablenodes() {
        return completestructuredactivities_executablenodes;
    }

    public void addCompletestructuredactivities_executablenode(Completestructuredactivities_executablenode completestructuredactivities_executablenode) {
        this.completestructuredactivities_executablenodes.add(completestructuredactivities_executablenode);
    }
    public BasicActions_OutputPin getBasicactions_outputpin() {
        return basicactions_outputpin;
    }

    public void setBasicactions_outputpin(BasicActions_OutputPin basicactions_outputpin) {
        this.basicactions_outputpin = basicactions_outputpin;
    }

}