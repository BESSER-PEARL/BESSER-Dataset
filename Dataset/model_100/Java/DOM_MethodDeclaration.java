





import java.util.List;
import java.util.ArrayList;

public class DOM_MethodDeclaration extends BodyDeclaration {

    private String varargs;
    private String extraDimensions;
    private String constructor;





    private IMethod imethod;




    private List<SingleVariableDeclaration> singlevariabledeclarations;


    public DOM_MethodDeclaration(
        String varargs,        String extraDimensions,        String constructor    ) {
        super(
        );
        this.varargs = varargs;
        this.extraDimensions = extraDimensions;
        this.constructor = constructor;
        this.singlevariabledeclarations = new ArrayList<>();
    }

    public DOM_MethodDeclaration(
        String varargs,        String extraDimensions,        String constructor        ArrayList<SingleVariableDeclaration> singlevariabledeclarations    ) {
        this.varargs = varargs;
        this.extraDimensions = extraDimensions;
        this.constructor = constructor;
        this.singlevariabledeclarations = singlevariabledeclarations;
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
    public List<SingleVariableDeclaration> getSinglevariabledeclarations() {
        return singlevariabledeclarations;
    }

    public void addSinglevariabledeclaration(Singlevariabledeclaration singlevariabledeclaration) {
        this.singlevariabledeclarations.add(singlevariabledeclaration);
    }

}