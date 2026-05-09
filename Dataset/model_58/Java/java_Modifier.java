





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private String visibility;
    private boolean transient;
    private boolean strictfp;
    private boolean static;
    private boolean synchronized;
    private boolean native;
    private String inheritance;
    private boolean volatile;





    private java_VariableDeclarationExpression java_variabledeclarationexpression;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private java_VariableDeclarationExpression java_variabledeclarationexpression;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;


    public java_Modifier(
        String visibility,        boolean transient,        boolean strictfp,        boolean static,        boolean synchronized,        boolean native,        String inheritance,        boolean volatile    ) {
        super(
        );
        this.visibility = visibility;
        this.transient = transient;
        this.strictfp = strictfp;
        this.static = static;
        this.synchronized = synchronized;
        this.native = native;
        this.inheritance = inheritance;
        this.volatile = volatile;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
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

}