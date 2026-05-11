





import java.util.List;
import java.util.ArrayList;

public class behavioral_elements_activity_graphs_ObjectFlowState extends SimpleState {

    private String isSynch;





    private List<Parameter> parameters;




    private Classifier classifier;


    public behavioral_elements_activity_graphs_ObjectFlowState(
        String isSynch    ) {
        super(
        );
        this.isSynch = isSynch;
        this.parameters = new ArrayList<>();
    }

    public behavioral_elements_activity_graphs_ObjectFlowState(
        String isSynch        ArrayList<Parameter> parameters    ) {
        this.isSynch = isSynch;
        this.parameters = parameters;
    }

    public String getIssynch() {
        return isSynch;
    }

    public void setIssynch(String isSynch) {
        this.isSynch = isSynch;
    }

    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }
    public Classifier getClassifier() {
        return classifier;
    }

    public void setClassifier(Classifier classifier) {
        this.classifier = classifier;
    }

}