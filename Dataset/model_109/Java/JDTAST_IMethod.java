





import java.util.List;
import java.util.ArrayList;

public class JDTAST_IMethod extends IMember {

    private String isConstructor;
    private String isMainMethod;
    private String exceptionTypes;
    private String returnType;





    private JDTAST_IType jdtast_itype;


    public JDTAST_IMethod(
        String isConstructor,        String isMainMethod,        String exceptionTypes,        String returnType    ) {
        super(
        );
        this.isConstructor = isConstructor;
        this.isMainMethod = isMainMethod;
        this.exceptionTypes = exceptionTypes;
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
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }

    public JDTAST_IType getJdtast_itype() {
        return jdtast_itype;
    }

    public void setJdtast_itype(JDTAST_IType jdtast_itype) {
        this.jdtast_itype = jdtast_itype;
    }

}