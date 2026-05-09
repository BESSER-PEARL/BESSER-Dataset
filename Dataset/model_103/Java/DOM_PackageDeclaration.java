





import java.util.List;
import java.util.ArrayList;

public class DOM_PackageDeclaration extends ASTNode {






    private Javadoc javadoc;




    private IPackageFragment ipackagefragment;


    public DOM_PackageDeclaration(
    ) {
        super(
        );
    }



    public Javadoc getJavadoc() {
        return javadoc;
    }

    public void setJavadoc(Javadoc javadoc) {
        this.javadoc = javadoc;
    }
    public IPackageFragment getIpackagefragment() {
        return ipackagefragment;
    }

    public void setIpackagefragment(IPackageFragment ipackagefragment) {
        this.ipackagefragment = ipackagefragment;
    }

}