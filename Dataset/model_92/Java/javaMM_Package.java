





import java.util.List;
import java.util.ArrayList;

public class javaMM_Package extends NamedElement {






    private List<javaMM_PackageAccess> javamm_packageaccesss;




    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;




    private javaMM_PackageAccess javamm_packageaccess;




    private javaMM_Package javamm_package;




    private javaMM_Model javamm_model;




    private javaMM_Package javamm_package;




    private List<javaMM_AbstractTypeDeclaration> javamm_abstracttypedeclarations;




    private javaMM_Model javamm_model;


    public javaMM_Package(
    ) {
        super(
        );
        this.javamm_packageaccesss = new ArrayList<>();
        this.javamm_abstracttypedeclarations = new ArrayList<>();
    }

    public javaMM_Package(
        ArrayList<javaMM_PackageAccess> javamm_packageaccesss,        ArrayList<javaMM_AbstractTypeDeclaration> javamm_abstracttypedeclarations    ) {
        this.javamm_packageaccesss = javamm_packageaccesss;
        this.javamm_abstracttypedeclarations = javamm_abstracttypedeclarations;
    }


    public List<javaMM_PackageAccess> getJavamm_packageaccesss() {
        return javamm_packageaccesss;
    }

    public void addJavamm_packageaccess(Javamm_packageaccess javamm_packageaccess) {
        this.javamm_packageaccesss.add(javamm_packageaccess);
    }
    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }
    public javaMM_PackageAccess getJavamm_packageaccess() {
        return javamm_packageaccess;
    }

    public void setJavamm_packageaccess(javaMM_PackageAccess javamm_packageaccess) {
        this.javamm_packageaccess = javamm_packageaccess;
    }
    public javaMM_Package getJavamm_package() {
        return javamm_package;
    }

    public void setJavamm_package(javaMM_Package javamm_package) {
        this.javamm_package = javamm_package;
    }
    public javaMM_Model getJavamm_model() {
        return javamm_model;
    }

    public void setJavamm_model(javaMM_Model javamm_model) {
        this.javamm_model = javamm_model;
    }
    public javaMM_Package getJavamm_package() {
        return javamm_package;
    }

    public void setJavamm_package(javaMM_Package javamm_package) {
        this.javamm_package = javamm_package;
    }
    public List<javaMM_AbstractTypeDeclaration> getJavamm_abstracttypedeclarations() {
        return javamm_abstracttypedeclarations;
    }

    public void addJavamm_abstracttypedeclaration(Javamm_abstracttypedeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclarations.add(javamm_abstracttypedeclaration);
    }
    public javaMM_Model getJavamm_model() {
        return javamm_model;
    }

    public void setJavamm_model(javaMM_Model javamm_model) {
        this.javamm_model = javamm_model;
    }

}