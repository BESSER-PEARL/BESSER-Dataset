





import java.util.List;
import java.util.ArrayList;

public class Java5_AbstractTypeDeclaration extends BodyDeclaration {

    private String qualifiedName;





    private Java5_CompilationUnit java5_compilationunit;




    private Java5_TypeDeclarationStatement java5_typedeclarationstatement;


    public Java5_AbstractTypeDeclaration(
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

    public Java5_CompilationUnit getJava5_compilationunit() {
        return java5_compilationunit;
    }

    public void setJava5_compilationunit(Java5_CompilationUnit java5_compilationunit) {
        this.java5_compilationunit = java5_compilationunit;
    }
    public Java5_TypeDeclarationStatement getJava5_typedeclarationstatement() {
        return java5_typedeclarationstatement;
    }

    public void setJava5_typedeclarationstatement(Java5_TypeDeclarationStatement java5_typedeclarationstatement) {
        this.java5_typedeclarationstatement = java5_typedeclarationstatement;
    }

}