





import java.util.List;
import java.util.ArrayList;

public class Java5_Modifier extends ASTNode {

    private String visibility;
    private String inheritance;
    private boolean static;
    private boolean volatile;
    private boolean native;
    private boolean strictfp;
    private boolean synchronized;
    private boolean transient;





    private Java5_VariableDeclarationExpression java5_variabledeclarationexpression;




    private Java5_BodyDeclaration java5_bodydeclaration;




    private Java5_SingleVariableDeclaration java5_singlevariabledeclaration;




    private Java5_VariableDeclarationStatement java5_variabledeclarationstatement;




    private Java5_VariableDeclarationExpression java5_variabledeclarationexpression;




    private Java5_SingleVariableDeclaration java5_singlevariabledeclaration;




    private Java5_VariableDeclarationStatement java5_variabledeclarationstatement;




    private Java5_BodyDeclaration java5_bodydeclaration;


    public Java5_Modifier(
        String visibility,        String inheritance,        boolean static,        boolean volatile,        boolean native,        boolean strictfp,        boolean synchronized,        boolean transient    ) {
        super(
        );
        this.visibility = visibility;
        this.inheritance = inheritance;
        this.static = static;
        this.volatile = volatile;
        this.native = native;
        this.strictfp = strictfp;
        this.synchronized = synchronized;
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
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }

    public Java5_VariableDeclarationExpression getJava5_variabledeclarationexpression() {
        return java5_variabledeclarationexpression;
    }

    public void setJava5_variabledeclarationexpression(Java5_VariableDeclarationExpression java5_variabledeclarationexpression) {
        this.java5_variabledeclarationexpression = java5_variabledeclarationexpression;
    }
    public Java5_BodyDeclaration getJava5_bodydeclaration() {
        return java5_bodydeclaration;
    }

    public void setJava5_bodydeclaration(Java5_BodyDeclaration java5_bodydeclaration) {
        this.java5_bodydeclaration = java5_bodydeclaration;
    }
    public Java5_SingleVariableDeclaration getJava5_singlevariabledeclaration() {
        return java5_singlevariabledeclaration;
    }

    public void setJava5_singlevariabledeclaration(Java5_SingleVariableDeclaration java5_singlevariabledeclaration) {
        this.java5_singlevariabledeclaration = java5_singlevariabledeclaration;
    }
    public Java5_VariableDeclarationStatement getJava5_variabledeclarationstatement() {
        return java5_variabledeclarationstatement;
    }

    public void setJava5_variabledeclarationstatement(Java5_VariableDeclarationStatement java5_variabledeclarationstatement) {
        this.java5_variabledeclarationstatement = java5_variabledeclarationstatement;
    }
    public Java5_VariableDeclarationExpression getJava5_variabledeclarationexpression() {
        return java5_variabledeclarationexpression;
    }

    public void setJava5_variabledeclarationexpression(Java5_VariableDeclarationExpression java5_variabledeclarationexpression) {
        this.java5_variabledeclarationexpression = java5_variabledeclarationexpression;
    }
    public Java5_SingleVariableDeclaration getJava5_singlevariabledeclaration() {
        return java5_singlevariabledeclaration;
    }

    public void setJava5_singlevariabledeclaration(Java5_SingleVariableDeclaration java5_singlevariabledeclaration) {
        this.java5_singlevariabledeclaration = java5_singlevariabledeclaration;
    }
    public Java5_VariableDeclarationStatement getJava5_variabledeclarationstatement() {
        return java5_variabledeclarationstatement;
    }

    public void setJava5_variabledeclarationstatement(Java5_VariableDeclarationStatement java5_variabledeclarationstatement) {
        this.java5_variabledeclarationstatement = java5_variabledeclarationstatement;
    }
    public Java5_BodyDeclaration getJava5_bodydeclaration() {
        return java5_bodydeclaration;
    }

    public void setJava5_bodydeclaration(Java5_BodyDeclaration java5_bodydeclaration) {
        this.java5_bodydeclaration = java5_bodydeclaration;
    }

}