





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Package extends TemplateableElement, Namespace, PackageableElement {

    private String nestingPackage;
    private String ownedType;
    private String nestedPackage;



    public UMLModel_Package(
        String nestingPackage,        String ownedType,        String nestedPackage    ) {
        super(
        );
        this.nestingPackage = nestingPackage;
        this.ownedType = ownedType;
        this.nestedPackage = nestedPackage;
    }


    public String getNestingpackage() {
        return nestingPackage;
    }

    public void setNestingpackage(String nestingPackage) {
        this.nestingPackage = nestingPackage;
    }
    public String getOwnedtype() {
        return ownedType;
    }

    public void setOwnedtype(String ownedType) {
        this.ownedType = ownedType;
    }
    public String getNestedpackage() {
        return nestedPackage;
    }

    public void setNestedpackage(String nestedPackage) {
        this.nestedPackage = nestedPackage;
    }


}