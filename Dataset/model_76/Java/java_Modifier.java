





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private boolean volatile;
    private String inheritance;
    private boolean strictfp;
    private boolean synchronized;
    private boolean native;
    private boolean static;
    private String visibility;
    private boolean transient;





    private java_BodyDeclaration java_bodydeclaration;




    private java_BodyDeclaration java_bodydeclaration;




    private java_VariableDeclarationExpression java_variabledeclarationexpression;




    private java_VariableDeclarationExpression java_variabledeclarationexpression;


    public java_Modifier(
        boolean volatile,        String inheritance,        boolean strictfp,        boolean synchronized,        boolean native,        boolean static,        String visibility,        boolean transient    ) {
        super(
        );
        this.volatile = volatile;
        this.inheritance = inheritance;
        this.strictfp = strictfp;
        this.synchronized = synchronized;
        this.native = native;
        this.static = static;
        this.visibility = visibility;
        this.transient = transient;
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
    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
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
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
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

    public java_BodyDeclaration getJava_bodydeclaration() {
        return java_bodydeclaration;
    }

    public void setJava_bodydeclaration(java_BodyDeclaration java_bodydeclaration) {
        this.java_bodydeclaration = java_bodydeclaration;
    }
    public java_BodyDeclaration getJava_bodydeclaration() {
        return java_bodydeclaration;
    }

    public void setJava_bodydeclaration(java_BodyDeclaration java_bodydeclaration) {
        this.java_bodydeclaration = java_bodydeclaration;
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

}