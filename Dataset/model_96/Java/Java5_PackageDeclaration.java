





import java.util.List;
import java.util.ArrayList;

public class Java5_PackageDeclaration extends NamedElement {

    private String qualifiedName;





    private Java5_Model java5_model;




    private Java5_CompilationUnit java5_compilationunit;




    private Java5_PackageDeclaration java5_packagedeclaration;


    public Java5_PackageDeclaration(
        String qualifiedName    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
    }


    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }

    public Java5_Model getJava5_model() {
        return java5_model;
    }

    public void setJava5_model(Java5_Model java5_model) {
        this.java5_model = java5_model;
    }
    public Java5_CompilationUnit getJava5_compilationunit() {
        return java5_compilationunit;
    }

    public void setJava5_compilationunit(Java5_CompilationUnit java5_compilationunit) {
        this.java5_compilationunit = java5_compilationunit;
    }
    public Java5_PackageDeclaration getJava5_packagedeclaration() {
        return java5_packagedeclaration;
    }

    public void setJava5_packagedeclaration(Java5_PackageDeclaration java5_packagedeclaration) {
        this.java5_packagedeclaration = java5_packagedeclaration;
    }

}