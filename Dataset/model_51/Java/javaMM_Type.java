





import java.util.List;
import java.util.ArrayList;

public class javaMM_Type extends NamedElement {






    private List<javaMM_TypeAccess> javamm_typeaccesss;




    private javaMM_TypeAccess javamm_typeaccess;


    public javaMM_Type(
    ) {
        super(
        );
        this.javamm_typeaccesss = new ArrayList<>();
    }

    public javaMM_Type(
        ArrayList<javaMM_TypeAccess> javamm_typeaccesss    ) {
        this.javamm_typeaccesss = javamm_typeaccesss;
    }


    public List<javaMM_TypeAccess> getJavamm_typeaccesss() {
        return javamm_typeaccesss;
    }

    public void addJavamm_typeaccess(Javamm_typeaccess javamm_typeaccess) {
        this.javamm_typeaccesss.add(javamm_typeaccess);
    }
    public javaMM_TypeAccess getJavamm_typeaccess() {
        return javamm_typeaccess;
    }

    public void setJavamm_typeaccess(javaMM_TypeAccess javamm_typeaccess) {
        this.javamm_typeaccess = javamm_typeaccess;
    }

}