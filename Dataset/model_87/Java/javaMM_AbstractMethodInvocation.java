





import java.util.List;
import java.util.ArrayList;

public class javaMM_AbstractMethodInvocation extends ASTNode {






    private List<javaMM_TypeAccess> javamm_typeaccesss;


    public javaMM_AbstractMethodInvocation(
    ) {
        super(
        );
        this.javamm_typeaccesss = new ArrayList<>();
    }

    public javaMM_AbstractMethodInvocation(
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