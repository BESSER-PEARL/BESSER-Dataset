





import java.util.List;
import java.util.ArrayList;

public class DOM_PackageDeclaration extends ASTNode {






    private IPackageFragment ipackagefragment;




    private Javadoc javadoc;


    public DOM_PackageDeclaration(
    ) {
        super(
        );
    }



    public IPackageFragment getIpackagefragment() {
        return ipackagefragment;
    }

    public void setIpackagefragment(IPackageFragment ipackagefragment) {
        this.ipackagefragment = ipackagefragment;
    }
    public Javadoc getJavadoc() {
        return javadoc;
    }

    public void setJavadoc(Javadoc javadoc) {
        this.javadoc = javadoc;
    }

}