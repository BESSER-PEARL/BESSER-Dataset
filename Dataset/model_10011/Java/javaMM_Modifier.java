





import java.util.List;
import java.util.ArrayList;

public class javaMM_Modifier extends ASTNode {

    private boolean native;
    private boolean volatile;
    private String inheritance;
    private String visibility;
    private boolean transient;
    private boolean static;
    private boolean strictfp;
    private boolean synchronized;





    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;


    public javaMM_Modifier(
        boolean native,        boolean volatile,        String inheritance,        String visibility,        boolean transient,        boolean static,        boolean strictfp,        boolean synchronized    ) {
        super(
        );
        this.native = native;
        this.volatile = volatile;
        this.inheritance = inheritance;
        this.visibility = visibility;
        this.transient = transient;
        this.static = static;
        this.strictfp = strictfp;
        this.synchronized = synchronized;
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