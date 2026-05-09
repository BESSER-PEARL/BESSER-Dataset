





import java.util.List;
import java.util.ArrayList;

public class Core_IMethod extends IMember {

    private String returnType;
    private String isConstructor;
    private String isMainMethod;
    private String exceptionTypes;



    public Core_IMethod(
        String returnType,        String isConstructor,        String isMainMethod,        String exceptionTypes    ) {
        super(
        );
        this.returnType = returnType;
        this.isConstructor = isConstructor;
        this.isMainMethod = isMainMethod;
        this.exceptionTypes = exceptionTypes;
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


}