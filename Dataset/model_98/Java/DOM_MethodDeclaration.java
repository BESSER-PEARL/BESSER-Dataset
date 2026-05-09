





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodDeclaration extends BodyDeclaration {

    private String extraDimensions;
    private String constructor;
    private String varargs;





    private IMethod imethod;


    public DOM_MethodDeclaration(
        String extraDimensions,        String constructor,        String varargs    ) {
        super(
        );
        this.extraDimensions = extraDimensions;
        this.constructor = constructor;
        this.varargs = varargs;
    }


    public String getExtradimensions() {
        return extraDimensions;
    }

    public void setExtradimensions(String extraDimensions) {
        this.extraDimensions = extraDimensions;
    }
    public String getConstructor() {
        return constructor;
    }

    public void setConstructor(String constructor) {
        this.constructor = constructor;
    }
    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
    }

    public IMethod getImethod() {
        return imethod;
    }

    public void setImethod(IMethod imethod) {
        this.imethod = imethod;
    }

}