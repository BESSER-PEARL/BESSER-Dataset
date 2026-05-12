





import java.util.List;
import java.util.ArrayList;

public class javaMM_Modifier extends ASTNode {

    private boolean transient;
    private String inheritance;
    private boolean strictfp;
    private boolean static;
    private boolean volatile;
    private boolean synchronized;
    private String visibility;
    private boolean native;





    private javaMM_BodyDeclaration javamm_bodydeclaration;




    private javaMM_BodyDeclaration javamm_bodydeclaration;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;


    public javaMM_Modifier(
        boolean transient,        String inheritance,        boolean strictfp,        boolean static,        boolean volatile,        boolean synchronized,        String visibility,        boolean native    ) {
        super(
        );
        this.transient = transient;
        this.inheritance = inheritance;
        this.strictfp = strictfp;
        this.static = static;
        this.volatile = volatile;
        this.synchronized = synchronized;
        this.visibility = visibility;
        this.native = native;
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
    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
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
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }

    public javaMM_BodyDeclaration getJavamm_bodydeclaration() {
        return javamm_bodydeclaration;
    }

    public void setJavamm_bodydeclaration(javaMM_BodyDeclaration javamm_bodydeclaration) {
        this.javamm_bodydeclaration = javamm_bodydeclaration;
    }
    public javaMM_BodyDeclaration getJavamm_bodydeclaration() {
        return javamm_bodydeclaration;
    }

    public void setJavamm_bodydeclaration(javaMM_BodyDeclaration javamm_bodydeclaration) {
        this.javamm_bodydeclaration = javamm_bodydeclaration;
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