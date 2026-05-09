





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private boolean transient;
    private boolean native;
    private boolean synchronized;
    private boolean static;
    private boolean strictfp;
    private boolean volatile;
    private String inheritance;
    private String visibility;





    private java_VariableDeclarationExpression java_variabledeclarationexpression;




    private java_VariableDeclarationExpression java_variabledeclarationexpression;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;


    public java_Modifier(
        boolean transient,        boolean native,        boolean synchronized,        boolean static,        boolean strictfp,        boolean volatile,        String inheritance,        String visibility    ) {
        super(
        );
        this.transient = transient;
        this.native = native;
        this.synchronized = synchronized;
        this.static = static;
        this.strictfp = strictfp;
        this.volatile = volatile;
        this.inheritance = inheritance;
        this.visibility = visibility;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
    }
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public java_VariableDeclarationExpression getJava_variabledeclarationexpression() {
        return java_variabledeclarationexpression;
    }

    public void setJava_variabledeclarationexpression(java_VariableDeclarationExpression java_variabledeclarationexpression) {
        this.java_variabledeclarationexpression = java_variabledeclarationexpression;
    }
    public java_VariableDeclarationExpression getJava_variabledeclarationexpression() {
        return java_variabledeclarationexpression;
    }

    public void setJava_variabledeclarationexpression(java_VariableDeclarationExpression java_variabledeclarationexpression) {
        this.java_variabledeclarationexpression = java_variabledeclarationexpression;
    }
    public java_SingleVariableDeclaration getJava_singlevariabledeclaration() {
        return java_singlevariabledeclaration;
    }

    public void setJava_singlevariabledeclaration(java_SingleVariableDeclaration java_singlevariabledeclaration) {
        this.java_singlevariabledeclaration = java_singlevariabledeclaration;
    }
    public java_SingleVariableDeclaration getJava_singlevariabledeclaration() {
        return java_singlevariabledeclaration;
    }

    public void setJava_singlevariabledeclaration(java_SingleVariableDeclaration java_singlevariabledeclaration) {
        this.java_singlevariabledeclaration = java_singlevariabledeclaration;
    }

}