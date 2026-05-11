





import java.util.List;
import java.util.ArrayList;

public class uppaal_templates_AbstractTemplate extends core_CommentableElement, core_NamedElement {






    private List<Parameter> parameters;


    public uppaal_templates_AbstractTemplate(
    ) {
        super(
        );
        this.parameters = new ArrayList<>();
    }

    public uppaal_templates_AbstractTemplate(
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