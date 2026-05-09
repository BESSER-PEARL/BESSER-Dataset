





import java.util.List;
import java.util.ArrayList;

public class java__Modifier extends ASTNode {

    private boolean strictfp;
    private String inheritance;
    private boolean static;
    private boolean volatile;
    private boolean synchronized;
    private boolean transient;
    private boolean native;
    private String visibility;





    private java__VariableDeclarationExpression java__variabledeclarationexpression;




    private java__VariableDeclarationStatement java__variabledeclarationstatement;




    private java__SingleVariableDeclaration java__singlevariabledeclaration;




    private java__VariableDeclarationExpression java__variabledeclarationexpression;




    private java__SingleVariableDeclaration java__singlevariabledeclaration;




    private java__VariableDeclarationStatement java__variabledeclarationstatement;


    public java__Modifier(
        boolean strictfp,        String inheritance,        boolean static,        boolean volatile,        boolean synchronized,        boolean transient,        boolean native,        String visibility    ) {
        super(
        );
        this.strictfp = strictfp;
        this.inheritance = inheritance;
        this.static = static;
        this.volatile = volatile;
        this.synchronized = synchronized;
        this.transient = transient;
        this.native = native;
        this.visibility = visibility;
    }


    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
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
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public java__VariableDeclarationExpression getJava__variabledeclarationexpression() {
        return java__variabledeclarationexpression;
    }

    public void setJava__variabledeclarationexpression(java__VariableDeclarationExpression java__variabledeclarationexpression) {
        this.java__variabledeclarationexpression = java__variabledeclarationexpression;
    }
    public java__VariableDeclarationStatement getJava__variabledeclarationstatement() {
        return java__variabledeclarationstatement;
    }

    public void setJava__variabledeclarationstatement(java__VariableDeclarationStatement java__variabledeclarationstatement) {
        this.java__variabledeclarationstatement = java__variabledeclarationstatement;
    }
    public java__SingleVariableDeclaration getJava__singlevariabledeclaration() {
        return java__singlevariabledeclaration;
    }

    public void setJava__singlevariabledeclaration(java__SingleVariableDeclaration java__singlevariabledeclaration) {
        this.java__singlevariabledeclaration = java__singlevariabledeclaration;
    }
    public java__VariableDeclarationExpression getJava__variabledeclarationexpression() {
        return java__variabledeclarationexpression;
    }

    public void setJava__variabledeclarationexpression(java__VariableDeclarationExpression java__variabledeclarationexpression) {
        this.java__variabledeclarationexpression = java__variabledeclarationexpression;
    }
    public java__SingleVariableDeclaration getJava__singlevariabledeclaration() {
        return java__singlevariabledeclaration;
    }

    public void setJava__singlevariabledeclaration(java__SingleVariableDeclaration java__singlevariabledeclaration) {
        this.java__singlevariabledeclaration = java__singlevariabledeclaration;
    }
    public java__VariableDeclarationStatement getJava__variabledeclarationstatement() {
        return java__variabledeclarationstatement;
    }

    public void setJava__variabledeclarationstatement(java__VariableDeclarationStatement java__variabledeclarationstatement) {
        this.java__variabledeclarationstatement = java__variabledeclarationstatement;
    }

}