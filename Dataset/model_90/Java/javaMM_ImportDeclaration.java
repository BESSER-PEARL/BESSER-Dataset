





import java.util.List;
import java.util.ArrayList;

public class javaMM_ImportDeclaration extends ASTNode {

    private boolean static;





    private javaMM_NamedElement javamm_namedelement;




    private javaMM_NamedElement javamm_namedelement;


    public javaMM_ImportDeclaration(
        boolean static    ) {
        super(
        );
        this.static = static;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }

    public javaMM_NamedElement getJavamm_namedelement() {
        return javamm_namedelement;
    }

    public void setJavamm_namedelement(javaMM_NamedElement javamm_namedelement) {
        this.javamm_namedelement = javamm_namedelement;
    }
    public javaMM_NamedElement getJavamm_namedelement() {
        return javamm_namedelement;
    }

    public void setJavamm_namedelement(javaMM_NamedElement javamm_namedelement) {
        this.javamm_namedelement = javamm_namedelement;
    }

}