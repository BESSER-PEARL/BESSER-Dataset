





import java.util.List;
import java.util.ArrayList;

public class Core_IMethod extends IMember {

    private String returnType;
    private String isMainMethod;
    private String exceptionTypes;
    private String isConstructor;





    private List<Parameter> parameters;


    public Core_IMethod(
        String returnType,        String isMainMethod,        String exceptionTypes,        String isConstructor    ) {
        super(
        );
        this.returnType = returnType;
        this.isMainMethod = isMainMethod;
        this.exceptionTypes = exceptionTypes;
        this.isConstructor = isConstructor;
        this.parameters = new ArrayList<>();
    }

    public Core_IMethod(
        String returnType,        String isMainMethod,        String exceptionTypes,        String isConstructor        ArrayList<Parameter> parameters    ) {
        this.returnType = returnType;
        this.isMainMethod = isMainMethod;
        this.exceptionTypes = exceptionTypes;
        this.isConstructor = isConstructor;
        this.parameters = parameters;
    }

    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getIsmainmethod() {
        return isMainMethod;
    }

    public void setIsmainmethod(String isMainMethod) {
        this.isMainMethod = isMainMethod;
    }
    public String getExceptiontypes() {
        return exceptionTypes;
    }

    public void setExceptiontypes(String exceptionTypes) {
        this.exceptionTypes = exceptionTypes;
    }
    public String getIsconstructor() {
        return isConstructor;
    }

    public void setIsconstructor(String isConstructor) {
        this.isConstructor = isConstructor;
    }

    public List<Parameter> getParameters() {
        return parameters;
    }

    public void addParameter(Parameter parameter) {
        this.parameters.add(parameter);
    }

}