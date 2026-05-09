





import java.util.List;
import java.util.ArrayList;

public class OCL_Operation extends MultiplicityElement, TypedElement {






    private List<Parameter> parameters;


    public OCL_Operation(
    ) {
        super(
        );
        this.parameters = new ArrayList<>();
    }

    public OCL_Operation(
        ArrayList<Parameter> parameters    ) {
        this.parameters = parameters;
    }


    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }

}