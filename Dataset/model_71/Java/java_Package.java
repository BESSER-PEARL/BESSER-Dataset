





import java.util.List;
import java.util.ArrayList;

public class java_Package extends NamedElement {






    private List<java_AbstractTypeDeclaration> java_abstracttypedeclarations;




    private java_Package java_package;




    private List<java_Package> java_packages;




    private java_AbstractTypeDeclaration java_abstracttypedeclaration;


    public java_Package(
    ) {
        super(
        );
        this.java_abstracttypedeclarations = new ArrayList<>();
        this.java_packages = new ArrayList<>();
    }

    public java_Package(
        ArrayList<java_AbstractTypeDeclaration> java_abstracttypedeclarations,        ArrayList<java_Package> java_packages    ) {
        this.java_abstracttypedeclarations = java_abstracttypedeclarations;
        this.java_packages = java_packages;
    }


    public List<java_AbstractTypeDeclaration> getJava_abstracttypedeclarations() {
        return java_abstracttypedeclarations;
    }

    public void addJava_abstracttypedeclaration(Java_abstracttypedeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclarations.add(java_abstracttypedeclaration);
    }
    public java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(java_Package java_package) {
        this.java_package = java_package;
    }
    public List<java_Package> getJava_packages() {
        return java_packages;
    }

    public void addJava_package(Java_package java_package) {
        this.java_packages.add(java_package);
    }
    public java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }

}