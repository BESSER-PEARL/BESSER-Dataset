





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ProfileApplication extends DirectedRelationship {

    private String isStrict;
    private String appliedProfile;
    private String applyingPackage;





    private UMLModel_Package umlmodel_package;


    public UMLModel_ProfileApplication(
        String isStrict,        String appliedProfile,        String applyingPackage    ) {
        super(
        );
        this.isStrict = isStrict;
        this.appliedProfile = appliedProfile;
        this.applyingPackage = applyingPackage;
    }


    public String getIsstrict() {
        return isStrict;
    }

    public void setIsstrict(String isStrict) {
        this.isStrict = isStrict;
    }
    public String getAppliedprofile() {
        return appliedProfile;
    }

    public void setAppliedprofile(String appliedProfile) {
        this.appliedProfile = appliedProfile;
    }
    public String getApplyingpackage() {
        return applyingPackage;
    }

    public void setApplyingpackage(String applyingPackage) {
        this.applyingPackage = applyingPackage;
    }

    public UMLModel_Package getUmlmodel_package() {
        return umlmodel_package;
    }

    public void setUmlmodel_package(UMLModel_Package umlmodel_package) {
        this.umlmodel_package = umlmodel_package;
    }

}