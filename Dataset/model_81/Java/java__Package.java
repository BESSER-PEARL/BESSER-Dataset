





import java.util.List;
import java.util.ArrayList;

public class java__Package extends NamedElement {






    private java__ClassFile java__classfile;




    private java__AbstractTypeDeclaration java__abstracttypedeclaration;




    private java__Package java__package;




    private java__Model java__model;




    private java__PackageAccess java__packageaccess;




    private List<java__AbstractTypeDeclaration> java__abstracttypedeclarations;




    private java__Model java__model;




    private java__CompilationUnit java__compilationunit;




    private java__Package java__package;




    private List<java__PackageAccess> java__packageaccesss;


    public java__Package(
    ) {
        super(
        );
        this.java__abstracttypedeclarations = new ArrayList<>();
        this.java__packageaccesss = new ArrayList<>();
    }

    public java__Package(
        ArrayList<java__AbstractTypeDeclaration> java__abstracttypedeclarations,        ArrayList<java__PackageAccess> java__packageaccesss    ) {
        this.java__abstracttypedeclarations = java__abstracttypedeclarations;
        this.java__packageaccesss = java__packageaccesss;
    }


    public java__ClassFile getJava__classfile() {
        return java__classfile;
    }

    public void setJava__classfile(java__ClassFile java__classfile) {
        this.java__classfile = java__classfile;
    }
    public java__AbstractTypeDeclaration getJava__abstracttypedeclaration() {
        return java__abstracttypedeclaration;
    }

    public void setJava__abstracttypedeclaration(java__AbstractTypeDeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclaration = java__abstracttypedeclaration;
    }
    public java__Package getJava__package() {
        return java__package;
    }

    public void setJava__package(java__Package java__package) {
        this.java__package = java__package;
    }
    public java__Model getJava__model() {
        return java__model;
    }

    public void setJava__model(java__Model java__model) {
        this.java__model = java__model;
    }
    public java__PackageAccess getJava__packageaccess() {
        return java__packageaccess;
    }

    public void setJava__packageaccess(java__PackageAccess java__packageaccess) {
        this.java__packageaccess = java__packageaccess;
    }
    public List<java__AbstractTypeDeclaration> getJava__abstracttypedeclarations() {
        return java__abstracttypedeclarations;
    }

    public void addJava__abstracttypedeclaration(Java__abstracttypedeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclarations.add(java__abstracttypedeclaration);
    }
    public java__Model getJava__model() {
        return java__model;
    }

    public void setJava__model(java__Model java__model) {
        this.java__model = java__model;
    }
    public java__CompilationUnit getJava__compilationunit() {
        return java__compilationunit;
    }

    public void setJava__compilationunit(java__CompilationUnit java__compilationunit) {
        this.java__compilationunit = java__compilationunit;
    }
    public java__Package getJava__package() {
        return java__package;
    }

    public void setJava__package(java__Package java__package) {
        this.java__package = java__package;
    }
    public List<java__PackageAccess> getJava__packageaccesss() {
        return java__packageaccesss;
    }

    public void addJava__packageaccess(Java__packageaccess java__packageaccess) {
        this.java__packageaccesss.add(java__packageaccess);
    }

}