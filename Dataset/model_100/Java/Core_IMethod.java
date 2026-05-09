





import java.util.List;
import java.util.ArrayList;

public class Core_IMethod extends IMember {

    private String isMainMethod;
    private String isConstructor;
    private String returnType;
    private String exceptionTypes;



    public Core_IMethod(
        String isMainMethod,        String isConstructor,        String returnType,        String exceptionTypes    ) {
        super(
        );
        this.isMainMethod = isMainMethod;
        this.isConstructor = isConstructor;
        this.returnType = returnType;
        this.exceptionTypes = exceptionTypes;
    }


    public String getIsmainmethod() {
        return isMainMethod;
    }

    public void setIsmainmethod(String isMainMethod) {
        this.isMainMethod = isMainMethod;
    }
    public String getIsconstructor() {
        return isConstructor;
    }

    public void setIsconstructor(String isConstructor) {
        this.isConstructor = isConstructor;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getExceptiontypes() {
        return exceptionTypes;
    }

    public void setExceptiontypes(String exceptionTypes) {
        this.exceptionTypes = exceptionTypes;
    }


}