





import java.util.List;
import java.util.ArrayList;

public class EMOF_Operation extends MultiplicityElement, TypedElement {






    private List<Type> types;




    private List<Parameter> parameters;




    private Class class;


    public EMOF_Operation(
    ) {
        super(
        );
        this.types = new ArrayList<>();
        this.parameters = new ArrayList<>();
    }

    public EMOF_Operation(
        ArrayList<Type> types,        ArrayList<Parameter> parameters    ) {
        this.types = types;
        this.parameters = parameters;
    }


    public List<Type> getTypes() {
        return types;
    }

    public void addType(Type type) {
        this.types.add(type);
    }
    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }
    public Class getClass() {
        return class;
    }

    public void setClass(Class class) {
        this.class = class;
    }

}