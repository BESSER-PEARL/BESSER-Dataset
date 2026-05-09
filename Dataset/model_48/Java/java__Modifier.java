





import java.util.List;
import java.util.ArrayList;

public class java__Modifier extends ASTNode {

    private String visibility;
    private boolean volatile;
    private boolean native;
    private String inheritance;
    private boolean synchronized;
    private boolean static;
    private boolean strictfp;
    private boolean transient;





    private java__SingleVariableDeclaration java__singlevariabledeclaration;




    private java__SingleVariableDeclaration java__singlevariabledeclaration;


    public java__Modifier(
        String visibility,        boolean volatile,        boolean native,        String inheritance,        boolean synchronized,        boolean static,        boolean strictfp,        boolean transient    ) {
        super(
        );
        this.visibility = visibility;
        this.volatile = volatile;
        this.native = native;
        this.inheritance = inheritance;
        this.synchronized = synchronized;
        this.static = static;
        this.strictfp = strictfp;
        this.transient = transient;
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
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }

    public java__SingleVariableDeclaration getJava__singlevariabledeclaration() {
        return java__singlevariabledeclaration;
    }

    public void setJava__singlevariabledeclaration(java__SingleVariableDeclaration java__singlevariabledeclaration) {
        this.java__singlevariabledeclaration = java__singlevariabledeclaration;
    }
    public java__SingleVariableDeclaration getJava__singlevariabledeclaration() {
        return java__singlevariabledeclaration;
    }

    public void setJava__singlevariabledeclaration(java__SingleVariableDeclaration java__singlevariabledeclaration) {
        this.java__singlevariabledeclaration = java__singlevariabledeclaration;
    }

}