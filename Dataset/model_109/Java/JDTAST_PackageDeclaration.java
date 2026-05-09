





import java.util.List;
import java.util.ArrayList;

public class JDTAST_PackageDeclaration extends ASTNode {






    private JDTAST_CompilationUnit jdtast_compilationunit;




    private JDTAST_IPackageFragment jdtast_ipackagefragment;


    public JDTAST_PackageDeclaration(
    ) {
        super(
        );
    }



    public JDTAST_CompilationUnit getJdtast_compilationunit() {
        return jdtast_compilationunit;
    }

    public void setJdtast_compilationunit(JDTAST_CompilationUnit jdtast_compilationunit) {
        this.jdtast_compilationunit = jdtast_compilationunit;
    }
    public JDTAST_IPackageFragment getJdtast_ipackagefragment() {
        return jdtast_ipackagefragment;
    }

    public void setJdtast_ipackagefragment(JDTAST_IPackageFragment jdtast_ipackagefragment) {
        this.jdtast_ipackagefragment = jdtast_ipackagefragment;
    }

}