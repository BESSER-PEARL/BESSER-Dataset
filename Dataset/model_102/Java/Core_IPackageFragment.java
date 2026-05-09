





import java.util.List;
import java.util.ArrayList;

public class Core_IPackageFragment extends PhysicalElement, IJavaElement {

    private String isDefaultPackage;



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


}