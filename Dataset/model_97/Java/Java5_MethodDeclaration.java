





import java.util.List;
import java.util.ArrayList;

public class Java5_MethodDeclaration extends BodyDeclaration {

    private boolean varargs;
    private int extraArrayDimensions;
    private boolean constructor;





    private List<Java5_MethodDeclaration> java5_methoddeclarations;




    private List<Java5_SingleVariableDeclaration> java5_singlevariabledeclarations;




    private Java5_SingleVariableDeclaration java5_singlevariabledeclaration;




    private Java5_MethodDeclaration java5_methoddeclaration;


    public Java5_MethodDeclaration(
        boolean varargs,        int extraArrayDimensions,        boolean constructor    ) {
        super(
        );
        this.varargs = varargs;
        this.extraArrayDimensions = extraArrayDimensions;
        this.constructor = constructor;
        this.java5_methoddeclarations = new ArrayList<>();
        this.java5_singlevariabledeclarations = new ArrayList<>();
    }

    public Java5_MethodDeclaration(
        boolean varargs,        int extraArrayDimensions,        boolean constructor        ArrayList<Java5_MethodDeclaration> java5_methoddeclarations,        ArrayList<Java5_SingleVariableDeclaration> java5_singlevariabledeclarations    ) {
        this.varargs = varargs;
        this.extraArrayDimensions = extraArrayDimensions;
        this.constructor = constructor;
        this.java5_methoddeclarations = java5_methoddeclarations;
        this.java5_singlevariabledeclarations = java5_singlevariabledeclarations;
    }

    public boolean getVarargs() {
        return varargs;
    }

    public void setVarargs(boolean varargs) {
        this.varargs = varargs;
    }
    public int getExtraarraydimensions() {
        return extraArrayDimensions;
    }

    public void setExtraarraydimensions(int extraArrayDimensions) {
        this.extraArrayDimensions = extraArrayDimensions;
    }
    public boolean getConstructor() {
        return constructor;
    }

    public void setConstructor(boolean constructor) {
        this.constructor = constructor;
    }

    public List<Java5_MethodDeclaration> getJava5_methoddeclarations() {
        return java5_methoddeclarations;
    }

    public void addJava5_methoddeclaration(Java5_methoddeclaration java5_methoddeclaration) {
        this.java5_methoddeclarations.add(java5_methoddeclaration);
    }
    public List<Java5_SingleVariableDeclaration> getJava5_singlevariabledeclarations() {
        return java5_singlevariabledeclarations;
    }

    public void addJava5_singlevariabledeclaration(Java5_singlevariabledeclaration java5_singlevariabledeclaration) {
        this.java5_singlevariabledeclarations.add(java5_singlevariabledeclaration);
    }
    public Java5_SingleVariableDeclaration getJava5_singlevariabledeclaration() {
        return java5_singlevariabledeclaration;
    }

    public void setJava5_singlevariabledeclaration(Java5_SingleVariableDeclaration java5_singlevariabledeclaration) {
        this.java5_singlevariabledeclaration = java5_singlevariabledeclaration;
    }
    public Java5_MethodDeclaration getJava5_methoddeclaration() {
        return java5_methoddeclaration;
    }

    public void setJava5_methoddeclaration(Java5_MethodDeclaration java5_methoddeclaration) {
        this.java5_methoddeclaration = java5_methoddeclaration;
    }

}