





import java.util.List;
import java.util.ArrayList;

public class Core_IMethod extends IMember {

    private String isConstructor;
    private String exceptionTypes;
    private String returnType;
    private String isMainMethod;





    private PrimitiveTypes_Core_IType primitivetypes_core_itype;


    public Core_IMethod(
        String isConstructor,        String exceptionTypes,        String returnType,        String isMainMethod    ) {
        super(
        );
        this.isConstructor = isConstructor;
        this.exceptionTypes = exceptionTypes;
        this.returnType = returnType;
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
    public String getIsmainmethod() {
        return isMainMethod;
    }

    public void setIsmainmethod(String isMainMethod) {
        this.isMainMethod = isMainMethod;
    }

    public PrimitiveTypes_Core_IType getPrimitivetypes_core_itype() {
        return primitivetypes_core_itype;
    }

    public void setPrimitivetypes_core_itype(PrimitiveTypes_Core_IType primitivetypes_core_itype) {
        this.primitivetypes_core_itype = primitivetypes_core_itype;
    }

}