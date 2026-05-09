





import java.util.List;
import java.util.ArrayList;

public class EMOF_Operation extends TypedElement, MultiplicityElement {






    private Class class;




    private List<Parameter> parameters;




    private List<Type> types;


    public EMOF_Operation(
    ) {
        super(
        );
        this.parameters = new ArrayList<>();
        this.types = new ArrayList<>();
    }

    public EMOF_Operation(
        ArrayList<Parameter> parameters,        ArrayList<Type> types    ) {
        this.parameters = parameters;
        this.types = types;
    }


    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }
    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }
    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }

}