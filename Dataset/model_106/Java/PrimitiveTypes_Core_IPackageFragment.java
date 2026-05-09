





import java.util.List;
import java.util.ArrayList;

public class PrimitiveTypes_Core_IPackageFragment extends Core_IJavaElement, Core_PhysicalElement {

    private String isDefaultPackage;



    public PrimitiveTypes_Core_IPackageFragment(
        String isDefaultPackage    ) {
        super(
            String,            elementName,            String,            isReadOnly,            String,            path        );
        this.isDefaultPackage = isDefaultPackage;
    }


    public String getIsdefaultpackage() {
        return isDefaultPackage;
    }

    public void setIsdefaultpackage(String isDefaultPackage) {
        this.isDefaultPackage = isDefaultPackage;
    }


}