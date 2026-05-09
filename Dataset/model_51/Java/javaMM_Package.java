





import java.util.List;
import java.util.ArrayList;

public class javaMM_Package extends NamedElement {






    private javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration;




    private List<javaMM_AbstractTypeDeclaration> javamm_abstracttypedeclarations;




    private javaMM_Package javamm_package;




    private List<javaMM_Package> javamm_packages;


    public javaMM_Package(
    ) {
        super(
        );
        this.javamm_abstracttypedeclarations = new ArrayList<>();
        this.javamm_packages = new ArrayList<>();
    }

    public javaMM_Package(
        ArrayList<javaMM_AbstractTypeDeclaration> javamm_abstracttypedeclarations,        ArrayList<javaMM_Package> javamm_packages    ) {
        this.javamm_abstracttypedeclarations = javamm_abstracttypedeclarations;
        this.javamm_packages = javamm_packages;
    }


    public javaMM_AbstractTypeDeclaration getJavamm_abstracttypedeclaration() {
        return javamm_abstracttypedeclaration;
    }

    public void setJavamm_abstracttypedeclaration(javaMM_AbstractTypeDeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclaration = javamm_abstracttypedeclaration;
    }
    public List<javaMM_AbstractTypeDeclaration> getJavamm_abstracttypedeclarations() {
        return javamm_abstracttypedeclarations;
    }

    public void addJavamm_abstracttypedeclaration(Javamm_abstracttypedeclaration javamm_abstracttypedeclaration) {
        this.javamm_abstracttypedeclarations.add(javamm_abstracttypedeclaration);
    }
    public javaMM_Package getJavamm_package() {
        return javamm_package;
    }

    public void setJavamm_package(javaMM_Package javamm_package) {
        this.javamm_package = javamm_package;
    }
    public List<javaMM_Package> getJavamm_packages() {
        return javamm_packages;
    }

    public void addJavamm_package(Javamm_package javamm_package) {
        this.javamm_packages.add(javamm_package);
    }

}