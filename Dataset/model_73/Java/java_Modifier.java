





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private boolean native;
    private String visibility;
    private boolean synchronized;
    private boolean static;
    private boolean strictfp;
    private boolean volatile;
    private boolean transient;
    private String inheritance;





    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;


    public java_Modifier(
        boolean native,        String visibility,        boolean synchronized,        boolean static,        boolean strictfp,        boolean volatile,        boolean transient,        String inheritance    ) {
        super(
        );
        this.native = native;
        this.visibility = visibility;
        this.synchronized = synchronized;
        this.static = static;
        this.strictfp = strictfp;
        this.volatile = volatile;
        this.transient = transient;
        this.inheritance = inheritance;
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
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
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