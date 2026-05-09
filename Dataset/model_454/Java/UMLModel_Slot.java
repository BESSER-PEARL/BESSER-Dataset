





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Slot extends Element {

    private String owningInstance;
    private String definingFeature;





    private List<UMLModel_ValueSpecification> umlmodel_valuespecifications;




    private UMLModel_InstanceSpecification umlmodel_instancespecification;


    public UMLModel_Slot(
        String owningInstance,        String definingFeature    ) {
        super(
        );
        this.owningInstance = owningInstance;
        this.definingFeature = definingFeature;
        this.umlmodel_valuespecifications = new ArrayList<>();
    }

    public UMLModel_Slot(
        String owningInstance,        String definingFeature        ArrayList<UMLModel_ValueSpecification> umlmodel_valuespecifications    ) {
        this.owningInstance = owningInstance;
        this.definingFeature = definingFeature;
        this.umlmodel_valuespecifications = umlmodel_valuespecifications;
    }

    public String getOwninginstance() {
        return owningInstance;
    }

    public void setOwninginstance(String owningInstance) {
        this.owningInstance = owningInstance;
    }
    public String getDefiningfeature() {
        return definingFeature;
    }

    public void setDefiningfeature(String definingFeature) {
        this.definingFeature = definingFeature;
    }

    public List<UMLModel_ValueSpecification> getUmlmodel_valuespecifications() {
        return umlmodel_valuespecifications;
    }

    public void addUmlmodel_valuespecification(Umlmodel_valuespecification umlmodel_valuespecification) {
        this.umlmodel_valuespecifications.add(umlmodel_valuespecification);
    }
    public UMLModel_InstanceSpecification getUmlmodel_instancespecification() {
        return umlmodel_instancespecification;
    }

    public void setUmlmodel_instancespecification(UMLModel_InstanceSpecification umlmodel_instancespecification) {
        this.umlmodel_instancespecification = umlmodel_instancespecification;
    }

}