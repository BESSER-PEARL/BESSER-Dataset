





import java.util.List;
import java.util.ArrayList;

public class java__Modifier extends ASTNode {

    private boolean strictfp;
    private boolean synchronized;
    private boolean native;
    private String visibility;
    private boolean volatile;
    private boolean static;
    private String inheritance;
    private boolean transient;





    private java__BodyDeclaration java__bodydeclaration;




    private java__VariableDeclarationExpression java__variabledeclarationexpression;




    private java__SingleVariableDeclaration java__singlevariabledeclaration;




    private java__VariableDeclarationExpression java__variabledeclarationexpression;




    private java__BodyDeclaration java__bodydeclaration;




    private java__SingleVariableDeclaration java__singlevariabledeclaration;


    public java__Modifier(
        boolean strictfp,        boolean synchronized,        boolean native,        String visibility,        boolean volatile,        boolean static,        String inheritance,        boolean transient    ) {
        super(
        );
        this.strictfp = strictfp;
        this.synchronized = synchronized;
        this.native = native;
        this.visibility = visibility;
        this.volatile = volatile;
        this.static = static;
        this.inheritance = inheritance;
        this.transient = transient;
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
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }

    public java__BodyDeclaration getJava__bodydeclaration() {
        return java__bodydeclaration;
    }

    public void setJava__bodydeclaration(java__BodyDeclaration java__bodydeclaration) {
        this.java__bodydeclaration = java__bodydeclaration;
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
    public java__VariableDeclarationExpression getJava__variabledeclarationexpression() {
        return java__variabledeclarationexpression;
    }

    public void setJava__variabledeclarationexpression(java__VariableDeclarationExpression java__variabledeclarationexpression) {
        this.java__variabledeclarationexpression = java__variabledeclarationexpression;
    }
    public java__BodyDeclaration getJava__bodydeclaration() {
        return java__bodydeclaration;
    }

    public void setJava__bodydeclaration(java__BodyDeclaration java__bodydeclaration) {
        this.java__bodydeclaration = java__bodydeclaration;
    }
    public java__SingleVariableDeclaration getJava__singlevariabledeclaration() {
        return java__singlevariabledeclaration;
    }

    public void setJava__singlevariabledeclaration(java__SingleVariableDeclaration java__singlevariabledeclaration) {
        this.java__singlevariabledeclaration = java__singlevariabledeclaration;
    }

}