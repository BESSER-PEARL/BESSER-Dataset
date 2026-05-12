





import java.util.List;
import java.util.ArrayList;

public class javaMM_AbstractTypeDeclaration extends Type, BodyDeclaration {






    private List<javaMM_TypeAccess> javamm_typeaccesss;


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

}