





import java.util.List;
import java.util.ArrayList;

public class javaMM_MemberRef extends ASTNode {






    private javaMM_NamedElement javamm_namedelement;




    private javaMM_TypeAccess javamm_typeaccess;


    public javaMM_MemberRef(
    ) {
        super(
        );
    }



    public javaMM_NamedElement getJavamm_namedelement() {
        return javamm_namedelement;
    }

    public void setJavamm_namedelement(javaMM_NamedElement javamm_namedelement) {
        this.javamm_namedelement = javamm_namedelement;
    }
    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }

}