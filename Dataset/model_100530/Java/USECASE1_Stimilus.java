





import java.util.List;
import java.util.ArrayList;

public class USECASE1_Stimilus extends Event {






    private List<Parameter> parameters;


    public USECASE1_Stimilus(
    ) {
        super(
        );
        this.parameters = new ArrayList<>();
    }

    public USECASE1_Stimilus(
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