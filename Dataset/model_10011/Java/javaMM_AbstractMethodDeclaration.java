





import java.util.List;
import java.util.ArrayList;

public class javaMM_AbstractMethodDeclaration extends BodyDeclaration {






    private List<javaMM_TypeParameter> javamm_typeparameters;




    private List<javaMM_TypeAccess> javamm_typeaccesss;




    private javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration;




    private List<javaMM_SingleVariableDeclaration> javamm_singlevariabledeclarations;


    public javaMM_AbstractMethodDeclaration(
    ) {
        super(
        );
        this.javamm_typeparameters = new ArrayList<>();
        this.javamm_typeaccesss = new ArrayList<>();
        this.javamm_singlevariabledeclarations = new ArrayList<>();
    }

    public javaMM_AbstractMethodDeclaration(
        ArrayList<javaMM_TypeParameter> javamm_typeparameters,        ArrayList<javaMM_TypeAccess> javamm_typeaccesss,        ArrayList<javaMM_SingleVariableDeclaration> javamm_singlevariabledeclarations    ) {
        this.javamm_typeparameters = javamm_typeparameters;
        this.javamm_typeaccesss = javamm_typeaccesss;
        this.javamm_singlevariabledeclarations = javamm_singlevariabledeclarations;
    }


    public List<javaMM_TypeParameter> getJavamm_typeparameters() {
        return javamm_typeparameters;
    }

    public void addJavamm_typeparameter(Javamm_typeparameter javamm_typeparameter) {
        this.javamm_typeparameters.add(javamm_typeparameter);
    }
    public List<javaMM_TypeAccess> getJavamm_typeaccesss() {
        return javamm_typeaccesss;
    }

    public void addJavamm_typeaccess(Javamm_typeaccess javamm_typeaccess) {
        this.javamm_typeaccesss.add(javamm_typeaccess);
    }
    public javaMM_SingleVariableDeclaration getJavamm_singlevariabledeclaration() {
        return javamm_singlevariabledeclaration;
    }

    public void setJavamm_singlevariabledeclaration(javaMM_SingleVariableDeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclaration = javamm_singlevariabledeclaration;
    }
    public List<javaMM_SingleVariableDeclaration> getJavamm_singlevariabledeclarations() {
        return javamm_singlevariabledeclarations;
    }

    public void addJavamm_singlevariabledeclaration(Javamm_singlevariabledeclaration javamm_singlevariabledeclaration) {
        this.javamm_singlevariabledeclarations.add(javamm_singlevariabledeclaration);
    }

}