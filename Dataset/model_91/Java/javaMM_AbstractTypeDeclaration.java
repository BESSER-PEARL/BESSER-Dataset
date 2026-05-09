





import java.util.List;
import java.util.ArrayList;

public class javaMM_AbstractTypeDeclaration extends BodyDeclaration, Type {






    private List<javaMM_TypeAccess> javamm_typeaccesss;




    private javaMM_TypeDeclarationStatement javamm_typedeclarationstatement;


    public javaMM_AbstractTypeDeclaration(
    ) {
        super(
        );
        this.javamm_typeaccesss = new ArrayList<>();
    }

    public javaMM_AbstractTypeDeclaration(
        ArrayList<javaMM_TypeAccess> javamm_typeaccesss    ) {
        this.javamm_typeaccesss = javamm_typeaccesss;
    }


    public List<javaMM_TypeAccess> getJavamm_typeaccesss() {
        return javamm_typeaccesss;
    }

    public void addJavamm_typeaccess(Javamm_typeaccess javamm_typeaccess) {
        this.javamm_typeaccesss.add(javamm_typeaccess);
    }
    public javaMM_TypeDeclarationStatement getJavamm_typedeclarationstatement() {
        return javamm_typedeclarationstatement;
    }

    public void setJavamm_typedeclarationstatement(javaMM_TypeDeclarationStatement javamm_typedeclarationstatement) {
        this.javamm_typedeclarationstatement = javamm_typedeclarationstatement;
    }

}