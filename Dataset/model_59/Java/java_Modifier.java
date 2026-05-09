





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private boolean transient;
    private boolean volatile;
    private boolean synchronized;
    private boolean strictfp;
    private boolean native;
    private String visibility;
    private String inheritance;
    private boolean static;





    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private java_VariableDeclarationExpression java_variabledeclarationexpression;




    private java_VariableDeclarationExpression java_variabledeclarationexpression;




    private java_BodyDeclaration java_bodydeclaration;




    private java_BodyDeclaration java_bodydeclaration;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;


    public java_Modifier(
        boolean transient,        boolean volatile,        boolean synchronized,        boolean strictfp,        boolean native,        String visibility,        String inheritance,        boolean static    ) {
        super(
        );
        this.transient = transient;
        this.volatile = volatile;
        this.synchronized = synchronized;
        this.strictfp = strictfp;
        this.native = native;
        this.visibility = visibility;
        this.inheritance = inheritance;
        this.static = static;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
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
    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
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
    public java_VariableDeclarationExpression getJava_variabledeclarationexpression() {
        return java_variabledeclarationexpression;
    }

    public void setJava_variabledeclarationexpression(java_VariableDeclarationExpression java_variabledeclarationexpression) {
        this.java_variabledeclarationexpression = java_variabledeclarationexpression;
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
    public java_SingleVariableDeclaration getJava_singlevariabledeclaration() {
        return java_singlevariabledeclaration;
    }

    public void setJava_singlevariabledeclaration(java_SingleVariableDeclaration java_singlevariabledeclaration) {
        this.java_singlevariabledeclaration = java_singlevariabledeclaration;
    }

}