





import java.util.List;
import java.util.ArrayList;

public class javaMM_TypeParameter extends Type {






    private javaMM_TypeDeclaration javamm_typedeclaration;




    private List<javaMM_TypeAccess> javamm_typeaccesss;


    public javaMM_TypeParameter(
    ) {
        super(
        );
        this.javamm_typeaccesss = new ArrayList<>();
    }

    public javaMM_TypeParameter(
        ArrayList<javaMM_TypeAccess> javamm_typeaccesss    ) {
        this.javamm_typeaccesss = javamm_typeaccesss;
    }


    public javaMM_TypeDeclaration getJavamm_typedeclaration() {
        return javamm_typedeclaration;
    }

    public void setJavamm_typedeclaration(javaMM_TypeDeclaration javamm_typedeclaration) {
        this.javamm_typedeclaration = javamm_typedeclaration;
    }
    public List<javaMM_TypeAccess> getJavamm_typeaccesss() {
        return javamm_typeaccesss;
    }

    public void addJavamm_typeaccess(Javamm_typeaccess javamm_typeaccess) {
        this.javamm_typeaccesss.add(javamm_typeaccess);
    }

}