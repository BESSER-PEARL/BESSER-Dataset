





import java.util.List;
import java.util.ArrayList;

public class Java_Package extends NamedElement {






    private List<Java_Package> java_packages;




    private Java_Package java_package;




    private Java_AbstractTypeDeclaration java_abstracttypedeclaration;




    private List<Java_AbstractTypeDeclaration> java_abstracttypedeclarations;


    public Java_Package(
    ) {
        super(
        );
        this.java_packages = new ArrayList<>();
        this.java_abstracttypedeclarations = new ArrayList<>();
    }

    public Java_Package(
        ArrayList<Java_Package> java_packages,        ArrayList<Java_AbstractTypeDeclaration> java_abstracttypedeclarations    ) {
        this.java_packages = java_packages;
        this.java_abstracttypedeclarations = java_abstracttypedeclarations;
    }


    public List<Java_Package> getJava_packages() {
        return java_packages;
    }

    public void addJava_package(Java_package java_package) {
        this.java_packages.add(java_package);
    }
    public Java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(Java_Package java_package) {
        this.java_package = java_package;
    }
    public Java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(Java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }
    public List<Java_AbstractTypeDeclaration> getJava_abstracttypedeclarations() {
        return java_abstracttypedeclarations;
    }

    public void addJava_abstracttypedeclaration(Java_abstracttypedeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclarations.add(java_abstracttypedeclaration);
    }

}