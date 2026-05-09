





import java.util.List;
import java.util.ArrayList;

public class java_Package extends NamedElement {






    private List<java_AbstractTypeDeclaration> java_abstracttypedeclarations;




    private java_Package java_package;




    private java_AbstractTypeDeclaration java_abstracttypedeclaration;




    private java_Package java_package;


    public java_Package(
    ) {
        super(
        );
        this.java_abstracttypedeclarations = new ArrayList<>();
    }

    public java_Package(
        ArrayList<java_AbstractTypeDeclaration> java_abstracttypedeclarations    ) {
        this.java_abstracttypedeclarations = java_abstracttypedeclarations;
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
    public java_AbstractTypeDeclaration getJava_abstracttypedeclaration() {
        return java_abstracttypedeclaration;
    }

    public void setJava_abstracttypedeclaration(java_AbstractTypeDeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclaration = java_abstracttypedeclaration;
    }
    public java_Package getJava_package() {
        return java_package;
    }

    public void setJava_package(java_Package java_package) {
        this.java_package = java_package;
    }

}