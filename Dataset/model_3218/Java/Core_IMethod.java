





import java.util.List;
import java.util.ArrayList;

public class Core_IMethod extends IMember {

    private String exceptionTypes;
    private String isMainMethod;
    private String returnType;
    private String isConstructor;





    private Core_IType core_itype;




    private List<Core_Parameter> core_parameters;


    public Core_IMethod(
        String exceptionTypes,        String isMainMethod,        String returnType,        String isConstructor    ) {
        super(
        );
        this.exceptionTypes = exceptionTypes;
        this.isMainMethod = isMainMethod;
        this.returnType = returnType;
        this.isConstructor = isConstructor;
        this.core_parameters = new ArrayList<>();
    }

    public Core_IMethod(
        String exceptionTypes,        String isMainMethod,        String returnType,        String isConstructor        ArrayList<Core_Parameter> core_parameters    ) {
        this.exceptionTypes = exceptionTypes;
        this.isMainMethod = isMainMethod;
        this.returnType = returnType;
        this.isConstructor = isConstructor;
        this.core_parameters = core_parameters;
    }

    public String getExceptiontypes() {
        return exceptionTypes;
    }

    public void setExceptiontypes(String exceptionTypes) {
        this.exceptionTypes = exceptionTypes;
    }
    public String getIsmainmethod() {
        return isMainMethod;
    }

    public void setIsmainmethod(String isMainMethod) {
        this.isMainMethod = isMainMethod;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getIsconstructor() {
        return isConstructor;
    }

    public void setIsconstructor(String isConstructor) {
        this.isConstructor = isConstructor;
    }

    public Core_IType getCore_itype() {
        return core_itype;
    }

    public void setCore_itype(Core_IType core_itype) {
        this.core_itype = core_itype;
    }
    public List<Core_Parameter> getCore_parameters() {
        return core_parameters;
    }

    public void addCore_parameter(Core_parameter core_parameter) {
        this.core_parameters.add(core_parameter);
    }

}