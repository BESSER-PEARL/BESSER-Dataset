





import java.util.List;
import java.util.ArrayList;

public class Core_IPackageFragment extends PhysicalElement, IJavaElement {

    private String isDefaultPackage;





    private PrimitiveTypes_Core_IPackageFragmentRoot primitivetypes_core_ipackagefragmentroot;


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

    public PrimitiveTypes_Core_IPackageFragmentRoot getPrimitivetypes_core_ipackagefragmentroot() {
        return primitivetypes_core_ipackagefragmentroot;
    }

    public void setPrimitivetypes_core_ipackagefragmentroot(PrimitiveTypes_Core_IPackageFragmentRoot primitivetypes_core_ipackagefragmentroot) {
        this.primitivetypes_core_ipackagefragmentroot = primitivetypes_core_ipackagefragmentroot;
    }

}