





import java.util.List;
import java.util.ArrayList;

public class jcl_containers_JobUnit extends containers_JCLRoot, commons_NamedElement, commons_IncompleteElement {






    private List<Parameter> parameters;




    private Literal literal;


    public jcl_containers_JobUnit(
    ) {
        super(
        );
        this.parameters = new ArrayList<>();
    }

    public jcl_containers_JobUnit(
        ArrayList<Parameter> parameters    ) {
        this.parameters = parameters;
    }


    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }
    public Literal getLiteral() {
        return literal;
    }

    public void setLiteral(Literal literal) {
        this.literal = literal;
    }

}