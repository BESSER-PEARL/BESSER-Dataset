





import java.util.List;
import java.util.ArrayList;

public class UMLModel_PackageMerge extends DirectedRelationship {

    private String mergedPackage;
    private String receivingPackage;





    private UMLModel_Package umlmodel_package;


    public UMLModel_PackageMerge(
        String mergedPackage,        String receivingPackage    ) {
        super(
        );
        this.mergedPackage = mergedPackage;
        this.receivingPackage = receivingPackage;
    }


    public String getMergedpackage() {
        return mergedPackage;
    }

    public void setMergedpackage(String mergedPackage) {
        this.mergedPackage = mergedPackage;
    }
    public String getReceivingpackage() {
        return receivingPackage;
    }

    public void setReceivingpackage(String receivingPackage) {
        this.receivingPackage = receivingPackage;
    }

    public UMLModel_Package getUmlmodel_package() {
        return umlmodel_package;
    }

    public void setUmlmodel_package(UMLModel_Package umlmodel_package) {
        this.umlmodel_package = umlmodel_package;
    }

}