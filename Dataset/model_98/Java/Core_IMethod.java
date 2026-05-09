





import java.util.List;
import java.util.ArrayList;

public class Core_IMethod extends IMember {

    private String isMainMethod;
    private String isConstructor;
    private String exceptionTypes;
    private String returnType;



    public Core_IMethod(
        String isMainMethod,        String isConstructor,        String exceptionTypes,        String returnType    ) {
        super(
        );
        this.isMainMethod = isMainMethod;
        this.isConstructor = isConstructor;
        this.exceptionTypes = exceptionTypes;
        this.returnType = returnType;
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
    public String getExceptiontypes() {
        return exceptionTypes;
    }

    public void setExceptiontypes(String exceptionTypes) {
        this.exceptionTypes = exceptionTypes;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }


}