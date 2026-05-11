





import java.util.List;
import java.util.ArrayList;

public class aadl2_ComponentTypeRename extends NamedElement {

    private String category;





    private aadl2_ComponentType aadl2_componenttype;




    private aadl2_PackageSection aadl2_packagesection;


    public aadl2_ComponentTypeRename(
        String category    ) {
        super(
        );
        this.category = category;
    }


    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }

    public aadl2_ComponentType getAadl2_componenttype() {
        return aadl2_componenttype;
    }

    public void setAadl2_componenttype(aadl2_ComponentType aadl2_componenttype) {
        this.aadl2_componenttype = aadl2_componenttype;
    }
    public aadl2_PackageSection getAadl2_packagesection() {
        return aadl2_packagesection;
    }

    public void setAadl2_packagesection(aadl2_PackageSection aadl2_packagesection) {
        this.aadl2_packagesection = aadl2_packagesection;
    }

}