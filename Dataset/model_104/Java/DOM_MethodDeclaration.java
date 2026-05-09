





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodDeclaration extends BodyDeclaration {

    private String varargs;
    private String extraDimensions;
    private String constructor;





    private IMethod imethod;


    public DOM_MethodDeclaration(
        String varargs,        String extraDimensions,        String constructor    ) {
        super(
        );
        this.varargs = varargs;
        this.extraDimensions = extraDimensions;
        this.constructor = constructor;
    }


    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
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

    public IMethod getImethod() {
        return imethod;
    }

    public void setImethod(IMethod imethod) {
        this.imethod = imethod;
    }

}