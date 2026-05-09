





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private boolean strictfp;
    private boolean native;
    private boolean volatile;
    private boolean synchronized;
    private String inheritance;
    private String visibility;
    private boolean transient;
    private boolean static;





    private java_SingleVariableDeclaration java_singlevariabledeclaration;




    private java_BodyDeclaration java_bodydeclaration;




    private java_BodyDeclaration java_bodydeclaration;




    private java_SingleVariableDeclaration java_singlevariabledeclaration;


    public java_Modifier(
        boolean strictfp,        boolean native,        boolean volatile,        boolean synchronized,        String inheritance,        String visibility,        boolean transient,        boolean static    ) {
        super(
        );
        this.strictfp = strictfp;
        this.native = native;
        this.volatile = volatile;
        this.synchronized = synchronized;
        this.inheritance = inheritance;
        this.visibility = visibility;
        this.transient = transient;
        this.static = static;
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
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
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