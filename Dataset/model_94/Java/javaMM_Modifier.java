





import java.util.List;
import java.util.ArrayList;

public class javaMM_Modifier extends ASTNode {

    private String synchronized;
    private String static;
    private String inheritance;
    private String visibility;
    private String volatile;
    private String transient;
    private String strictfp;
    private String native;





    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_BodyDeclaration javamm_bodydeclaration;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_BodyDeclaration javamm_bodydeclaration;


    public javaMM_Modifier(
        String synchronized,        String static,        String inheritance,        String visibility,        String volatile,        String transient,        String strictfp,        String native    ) {
        super(
        );
        this.synchronized = synchronized;
        this.static = static;
        this.inheritance = inheritance;
        this.visibility = visibility;
        this.volatile = volatile;
        this.transient = transient;
        this.strictfp = strictfp;
        this.native = native;
    }


    public String getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(String synchronized) {
        this.synchronized = synchronized;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
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
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }
    public String getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(String strictfp) {
        this.strictfp = strictfp;
    }
    public String getNative() {
        return native;
    }

    public void setNative(String native) {
        this.native = native;
    }

    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
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
    public javaMM_BodyDeclaration getJavamm_bodydeclaration() {
        return javamm_bodydeclaration;
    }

    public void setJavamm_bodydeclaration(javaMM_BodyDeclaration javamm_bodydeclaration) {
        this.javamm_bodydeclaration = javamm_bodydeclaration;
    }

}