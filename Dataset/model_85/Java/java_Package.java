





import java.util.List;
import java.util.ArrayList;

public class java_Package extends NamedElement {






    private java_AbstractTypeDeclaration java_abstracttypedeclaration;




    private java_Package java_package;




    private java_Model java_model;




    private java_Model java_model;




    private java_PackageAccess java_packageaccess;




    private java_CompilationUnit java_compilationunit;




    private List<java_Package> java_packages;




    private List<java_AbstractTypeDeclaration> java_abstracttypedeclarations;


    public java_Package(
    ) {
        super(
        );
        this.java_packages = new ArrayList<>();
        this.java_abstracttypedeclarations = new ArrayList<>();
    }

    public java_Package(
        ArrayList<java_Package> java_packages,        ArrayList<java_AbstractTypeDeclaration> java_abstracttypedeclarations    ) {
        this.java_packages = java_packages;
        this.java_abstracttypedeclarations = java_abstracttypedeclarations;
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
    public java_Model getJava_model() {
        return java_model;
    }

    public void setJava_model(java_Model java_model) {
        this.java_model = java_model;
    }
    public java_Model getJava_model() {
        return java_model;
    }

    public void setJava_model(java_Model java_model) {
        this.java_model = java_model;
    }
    public java_PackageAccess getJava_packageaccess() {
        return java_packageaccess;
    }

    public void setJava_packageaccess(java_PackageAccess java_packageaccess) {
        this.java_packageaccess = java_packageaccess;
    }
    public java_CompilationUnit getJava_compilationunit() {
        return java_compilationunit;
    }

    public void setJava_compilationunit(java_CompilationUnit java_compilationunit) {
        this.java_compilationunit = java_compilationunit;
    }
    public List<java_Package> getJava_packages() {
        return java_packages;
    }

    public void addJava_package(Java_package java_package) {
        this.java_packages.add(java_package);
    }
    public List<java_AbstractTypeDeclaration> getJava_abstracttypedeclarations() {
        return java_abstracttypedeclarations;
    }

    public void addJava_abstracttypedeclaration(Java_abstracttypedeclaration java_abstracttypedeclaration) {
        this.java_abstracttypedeclarations.add(java_abstracttypedeclaration);
    }

}