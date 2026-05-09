





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Profile extends Package {

    private String metamodelReference;
    private String ownedStereotype;
    private String metaclassReference;



    public UMLModel_Profile(
        String metamodelReference,        String ownedStereotype,        String metaclassReference    ) {
        super(
        );
        this.metamodelReference = metamodelReference;
        this.ownedStereotype = ownedStereotype;
        this.metaclassReference = metaclassReference;
    }


    public String getMetamodelreference() {
        return metamodelReference;
    }

    public void setMetamodelreference(String metamodelReference) {
        this.metamodelReference = metamodelReference;
    }
    public String getOwnedstereotype() {
        return ownedStereotype;
    }

    public void setOwnedstereotype(String ownedStereotype) {
        this.ownedStereotype = ownedStereotype;
    }
    public String getMetaclassreference() {
        return metaclassReference;
    }

    public void setMetaclassreference(String metaclassReference) {
        this.metaclassReference = metaclassReference;
    }


}