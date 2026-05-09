





import java.util.List;
import java.util.ArrayList;

public class java__Package extends NamedElement {






    private List<java__AbstractTypeDeclaration> java__abstracttypedeclarations;




    private java__Package java__package;




    private java__CompilationUnit java__compilationunit;




    private java__AbstractTypeDeclaration java__abstracttypedeclaration;




    private java__ClassFile java__classfile;




    private List<java__Package> java__packages;


    public java__Package(
    ) {
        super(
        );
        this.java__abstracttypedeclarations = new ArrayList<>();
        this.java__packages = new ArrayList<>();
    }

    public java__Package(
        ArrayList<java__AbstractTypeDeclaration> java__abstracttypedeclarations,        ArrayList<java__Package> java__packages    ) {
        this.java__abstracttypedeclarations = java__abstracttypedeclarations;
        this.java__packages = java__packages;
    }


    public List<java__AbstractTypeDeclaration> getJava__abstracttypedeclarations() {
        return java__abstracttypedeclarations;
    }

    public void addJava__abstracttypedeclaration(Java__abstracttypedeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclarations.add(java__abstracttypedeclaration);
    }
    public java__Package getJava__package() {
        return java__package;
    }

    public void setJava__package(java__Package java__package) {
        this.java__package = java__package;
    }
    public java__CompilationUnit getJava__compilationunit() {
        return java__compilationunit;
    }

    public void setJava__compilationunit(java__CompilationUnit java__compilationunit) {
        this.java__compilationunit = java__compilationunit;
    }
    public java__AbstractTypeDeclaration getJava__abstracttypedeclaration() {
        return java__abstracttypedeclaration;
    }

    public void setJava__abstracttypedeclaration(java__AbstractTypeDeclaration java__abstracttypedeclaration) {
        this.java__abstracttypedeclaration = java__abstracttypedeclaration;
    }
    public java__ClassFile getJava__classfile() {
        return java__classfile;
    }

    public void setJava__classfile(java__ClassFile java__classfile) {
        this.java__classfile = java__classfile;
    }
    public List<java__Package> getJava__packages() {
        return java__packages;
    }

    public void addJava__package(Java__package java__package) {
        this.java__packages.add(java__package);
    }

}