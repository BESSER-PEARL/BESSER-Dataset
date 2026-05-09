





import java.util.List;
import java.util.ArrayList;

public class Java5_AbstractTypeDeclaration extends BodyDeclaration {

    private String qualifiedName;





    private Java5_TypeDeclarationStatement java5_typedeclarationstatement;




    private Java5_BodyDeclaration java5_bodydeclaration;




    private Java5_PackageDeclaration java5_packagedeclaration;




    private List<Java5_ImportDeclaration> java5_importdeclarations;




    private Java5_CompilationUnit java5_compilationunit;




    private Java5_PackageDeclaration java5_packagedeclaration;




    private List<Java5_BodyDeclaration> java5_bodydeclarations;




    private List<Java5_NamedElementRef> java5_namedelementrefs;


    public Java5_AbstractTypeDeclaration(
        String qualifiedName    ) {
        super(
        );
        this.qualifiedName = qualifiedName;
        this.java5_importdeclarations = new ArrayList<>();
        this.java5_bodydeclarations = new ArrayList<>();
        this.java5_namedelementrefs = new ArrayList<>();
    }

    public Java5_AbstractTypeDeclaration(
        String qualifiedName        ArrayList<Java5_ImportDeclaration> java5_importdeclarations,        ArrayList<Java5_BodyDeclaration> java5_bodydeclarations,        ArrayList<Java5_NamedElementRef> java5_namedelementrefs    ) {
        this.qualifiedName = qualifiedName;
        this.java5_importdeclarations = java5_importdeclarations;
        this.java5_bodydeclarations = java5_bodydeclarations;
        this.java5_namedelementrefs = java5_namedelementrefs;
    }

    public String getQualifiedname() {
        return qualifiedName;
    }

    public void setQualifiedname(String qualifiedName) {
        this.qualifiedName = qualifiedName;
    }

    public Java5_TypeDeclarationStatement getJava5_typedeclarationstatement() {
        return java5_typedeclarationstatement;
    }

    public void setJava5_typedeclarationstatement(Java5_TypeDeclarationStatement java5_typedeclarationstatement) {
        this.java5_typedeclarationstatement = java5_typedeclarationstatement;
    }
    public Java5_BodyDeclaration getJava5_bodydeclaration() {
        return java5_bodydeclaration;
    }

    public void setJava5_bodydeclaration(Java5_BodyDeclaration java5_bodydeclaration) {
        this.java5_bodydeclaration = java5_bodydeclaration;
    }
    public Java5_PackageDeclaration getJava5_packagedeclaration() {
        return java5_packagedeclaration;
    }

    public void setJava5_packagedeclaration(Java5_PackageDeclaration java5_packagedeclaration) {
        this.java5_packagedeclaration = java5_packagedeclaration;
    }
    public List<Java5_ImportDeclaration> getJava5_importdeclarations() {
        return java5_importdeclarations;
    }

    public void addJava5_importdeclaration(Java5_importdeclaration java5_importdeclaration) {
        this.java5_importdeclarations.add(java5_importdeclaration);
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
    public List<Java5_BodyDeclaration> getJava5_bodydeclarations() {
        return java5_bodydeclarations;
    }

    public void addJava5_bodydeclaration(Java5_bodydeclaration java5_bodydeclaration) {
        this.java5_bodydeclarations.add(java5_bodydeclaration);
    }
    public List<Java5_NamedElementRef> getJava5_namedelementrefs() {
        return java5_namedelementrefs;
    }

    public void addJava5_namedelementref(Java5_namedelementref java5_namedelementref) {
        this.java5_namedelementrefs.add(java5_namedelementref);
    }

}