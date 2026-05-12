





import java.util.List;
import java.util.ArrayList;

public class Core_BehavioralFeature extends Feature {

    private String isQuery;





    private List<Parameter> parameters;


    public Core_BehavioralFeature(
        String isQuery    ) {
        super(
        );
        this.isQuery = isQuery;
        this.parameters = new ArrayList<>();
    }

    public Core_BehavioralFeature(
        String isQuery        ArrayList<Parameter> parameters    ) {
        this.isQuery = isQuery;
        this.parameters = parameters;
    }

    public String getIsquery() {
        return isQuery;
    }

    public void setIsquery(String isQuery) {
        this.isQuery = isQuery;
    }

    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }

}