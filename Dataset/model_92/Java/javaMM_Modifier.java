





import java.util.List;
import java.util.ArrayList;

public class javaMM_Modifier extends ASTNode {

    private String visibility;
    private String inheritance;
    private boolean synchronized;
    private boolean strictfp;
    private boolean static;
    private boolean volatile;
    private boolean native;
    private boolean transient;





    private javaMM_VariableDeclarationStatement javamm_variabledeclarationstatement;




    private javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression;




    private javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private javaMM_VariableDeclarationStatement javamm_variabledeclarationstatement;


    public javaMM_Modifier(
        String visibility,        String inheritance,        boolean synchronized,        boolean strictfp,        boolean static,        boolean volatile,        boolean native,        boolean transient    ) {
        super(
        );
        this.visibility = visibility;
        this.inheritance = inheritance;
        this.synchronized = synchronized;
        this.strictfp = strictfp;
        this.static = static;
        this.volatile = volatile;
        this.native = native;
        this.transient = transient;
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
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }

    public javaMM_VariableDeclarationStatement getJavamm_variabledeclarationstatement() {
        return javamm_variabledeclarationstatement;
    }

    public void setJavamm_variabledeclarationstatement(javaMM_VariableDeclarationStatement javamm_variabledeclarationstatement) {
        this.javamm_variabledeclarationstatement = javamm_variabledeclarationstatement;
    }
    public javaMM_VariableDeclarationExpression getJavamm_variabledeclarationexpression() {
        return javamm_variabledeclarationexpression;
    }

    public void setJavamm_variabledeclarationexpression(javaMM_VariableDeclarationExpression javamm_variabledeclarationexpression) {
        this.javamm_variabledeclarationexpression = javamm_variabledeclarationexpression;
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
    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
    }
    public javaMM_VariableDeclarationStatement getJavamm_variabledeclarationstatement() {
        return javamm_variabledeclarationstatement;
    }

    public void setJavamm_variabledeclarationstatement(javaMM_VariableDeclarationStatement javamm_variabledeclarationstatement) {
        this.javamm_variabledeclarationstatement = javamm_variabledeclarationstatement;
    }

}