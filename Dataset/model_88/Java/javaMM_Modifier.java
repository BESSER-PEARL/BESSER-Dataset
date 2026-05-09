





import java.util.List;
import java.util.ArrayList;

public class javaMM_Modifier extends ASTNode {

    private boolean synchronized;
    private boolean native;
    private boolean strictfp;
    private boolean volatile;
    private boolean static;
    private String inheritance;
    private String visibility;
    private boolean transient;





    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;


    public javaMM_Modifier(
        boolean synchronized,        boolean native,        boolean strictfp,        boolean volatile,        boolean static,        String inheritance,        String visibility,        boolean transient    ) {
        super(
        );
        this.synchronized = synchronized;
        this.native = native;
        this.strictfp = strictfp;
        this.volatile = volatile;
        this.static = static;
        this.inheritance = inheritance;
        this.visibility = visibility;
        this.transient = transient;
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

    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
    }
    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
    }

}