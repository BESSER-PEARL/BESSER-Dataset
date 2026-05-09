





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private String visibility;
    private boolean volatile;
    private boolean static;
    private String inheritance;
    private boolean synchronized;
    private boolean transient;
    private boolean native;
    private boolean strictfp;





    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private java_VariableDeclarationExpression java_variabledeclarationexpression;




    private java_VariableDeclarationStatement java_variabledeclarationstatement;




    private java_VariableDeclarationStatement java_variabledeclarationstatement;




    private java_VariableDeclarationExpression java_variabledeclarationexpression;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;


    public java_Modifier(
        String visibility,        boolean volatile,        boolean static,        String inheritance,        boolean synchronized,        boolean transient,        boolean native,        boolean strictfp    ) {
        super(
        );
        this.visibility = visibility;
        this.volatile = volatile;
        this.static = static;
        this.inheritance = inheritance;
        this.synchronized = synchronized;
        this.transient = transient;
        this.native = native;
        this.strictfp = strictfp;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
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
    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
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
    public java_VariableDeclarationStatement getJava_variabledeclarationstatement() {
        return java_variabledeclarationstatement;
    }

    public void setJava_variabledeclarationstatement(java_VariableDeclarationStatement java_variabledeclarationstatement) {
        this.java_variabledeclarationstatement = java_variabledeclarationstatement;
    }
    public java_VariableDeclarationStatement getJava_variabledeclarationstatement() {
        return java_variabledeclarationstatement;
    }

    public void setJava_variabledeclarationstatement(java_VariableDeclarationStatement java_variabledeclarationstatement) {
        this.java_variabledeclarationstatement = java_variabledeclarationstatement;
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