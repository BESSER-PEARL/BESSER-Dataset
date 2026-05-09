





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_MethodDeclaration extends BodyDeclaration {

    private String constructor;
    private String extraDimensions;
    private String varargs;



    public JavaAbstractSyntax_MethodDeclaration(
        String constructor,        String extraDimensions,        String varargs    ) {
        super(
        );
        this.constructor = constructor;
        this.extraDimensions = extraDimensions;
        this.varargs = varargs;
    }


    public String getConstructor() {
        return constructor;
    }

    public void setConstructor(String constructor) {
        this.constructor = constructor;
    }
    public String getExtradimensions() {
        return extraDimensions;
    }

    public void setExtradimensions(String extraDimensions) {
        this.extraDimensions = extraDimensions;
    }
    public String getVarargs() {
        return varargs;
    }

    public void setVarargs(String varargs) {
        this.varargs = varargs;
    }


}