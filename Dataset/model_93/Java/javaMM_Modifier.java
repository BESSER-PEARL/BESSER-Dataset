





import java.util.List;
import java.util.ArrayList;

public class javaMM_Modifier extends ASTNode {

    private String inheritance;
    private String static;
    private String transient;
    private String visibility;
    private String native;
    private String volatile;
    private String strictfp;
    private String synchronized;





    private javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;


    public javaMM_Modifier(
        String inheritance,        String static,        String transient,        String visibility,        String native,        String volatile,        String strictfp,        String synchronized    ) {
        super(
        );
        this.inheritance = inheritance;
        this.static = static;
        this.transient = transient;
        this.visibility = visibility;
        this.native = native;
        this.volatile = volatile;
        this.strictfp = strictfp;
        this.synchronized = synchronized;
    }


    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getNative() {
        return native;
    }

    public void setNative(String native) {
        this.native = native;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(String strictfp) {
        this.strictfp = strictfp;
    }
    public String getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(String synchronized) {
        this.synchronized = synchronized;
    }

    public javaMM_VariableDeclarationExpression getJavamm_variabledeclarationexpression() {
        return javamm_variabledeclarationexpression;
    }

    public void setJavamm_variabledeclarationexpression(javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression) {
        this.javamm_variabledeclarationexpression = javamm_variabledeclarationexpression;
    }
    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
    }
    public javaMM_VariableDeclarationExpression getJavamm_variabledeclarationexpression() {
        return javamm_variabledeclarationexpression;
    }

    public void setJavamm_variabledeclarationexpression(javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression) {
        this.javamm_variabledeclarationexpression = javamm_variabledeclarationexpression;
    }
    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
    }

}