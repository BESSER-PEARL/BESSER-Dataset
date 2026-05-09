





import java.util.List;
import java.util.ArrayList;

public class Core_IPackageFragment extends IJavaElement, PhysicalElement {

    private String isDefaultPackage;





    private IPackageFragmentRoot ipackagefragmentroot;


    public Core_IPackageFragment(
        String isDefaultPackage    ) {
        super(
        );
        this.isDefaultPackage = isDefaultPackage;
    }


    public String getIsdefaultpackage() {
        return isDefaultPackage;
    }

    public void setIsdefaultpackage(String isDefaultPackage) {
        this.isDefaultPackage = isDefaultPackage;
    }

    public IPackageFragmentRoot getIpackagefragmentroot() {
        return ipackagefragmentroot;
    }

    public void setIpackagefragmentroot(IPackageFragmentRoot ipackagefragmentroot) {
        this.ipackagefragmentroot = ipackagefragmentroot;
    }

}