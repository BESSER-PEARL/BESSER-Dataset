





import java.util.List;
import java.util.ArrayList;

public class jcl_statements_Statement extends members_Member, commons_NamedElement {






    private List<Parameter> parameters;


    public jcl_statements_Statement(
    ) {
        super(
        );
        this.parameters = new ArrayList<>();
    }

    public jcl_statements_Statement(
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