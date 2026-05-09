





import java.util.List;
import java.util.ArrayList;

public class ecore_EClassNotMatching extends EClassifier {

    private boolean interface;
    private boolean abstract;





    private List<ecore_EClassNotMatching> ecore_eclassnotmatchings;




    private List<ecore_EOperation> ecore_eoperations;




    private List<ecore_EStructuralFeature> ecore_estructuralfeatures;




    private List<ecore_EStructuralFeature> ecore_estructuralfeatures;




    private ecore_EStructuralFeature ecore_estructuralfeature;




    private ecore_EClassNotMatching ecore_eclassnotmatching;




    private List<ecore_EOperation> ecore_eoperations;




    private ecore_EOperation ecore_eoperation;


    public ecore_EClassNotMatching(
        boolean interface,        boolean abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.ecore_eclassnotmatchings = new ArrayList<>();
        this.ecore_eoperations = new ArrayList<>();
        this.ecore_estructuralfeatures = new ArrayList<>();
        this.ecore_estructuralfeatures = new ArrayList<>();
        this.ecore_eoperations = new ArrayList<>();
    }

    public ecore_EClassNotMatching(
        boolean interface,        boolean abstract        ArrayList<ecore_EClassNotMatching> ecore_eclassnotmatchings,        ArrayList<ecore_EOperation> ecore_eoperations,        ArrayList<ecore_EStructuralFeature> ecore_estructuralfeatures,        ArrayList<ecore_EStructuralFeature> ecore_estructuralfeatures,        ArrayList<ecore_EOperation> ecore_eoperations    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.ecore_eclassnotmatchings = ecore_eclassnotmatchings;
        this.ecore_eoperations = ecore_eoperations;
        this.ecore_estructuralfeatures = ecore_estructuralfeatures;
        this.ecore_estructuralfeatures = ecore_estructuralfeatures;
        this.ecore_eoperations = ecore_eoperations;
    }

    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public List<ecore_EClassNotMatching> getEcore_eclassnotmatchings() {
        return ecore_eclassnotmatchings;
    }

    public void addEcore_eclassnotmatching(Ecore_eclassnotmatching ecore_eclassnotmatching) {
        this.ecore_eclassnotmatchings.add(ecore_eclassnotmatching);
    }
    public List<ecore_EOperation> getEcore_eoperations() {
        return ecore_eoperations;
    }

    public void addEcore_eoperation(Ecore_eoperation ecore_eoperation) {
        this.ecore_eoperations.add(ecore_eoperation);
    }
    public List<ecore_EStructuralFeature> getEcore_estructuralfeatures() {
        return ecore_estructuralfeatures;
    }

    public void addEcore_estructuralfeature(Ecore_estructuralfeature ecore_estructuralfeature) {
        this.ecore_estructuralfeatures.add(ecore_estructuralfeature);
    }
    public List<ecore_EStructuralFeature> getEcore_estructuralfeatures() {
        return ecore_estructuralfeatures;
    }

    public void addEcore_estructuralfeature(Ecore_estructuralfeature ecore_estructuralfeature) {
        this.ecore_estructuralfeatures.add(ecore_estructuralfeature);
    }
    public ecore_EStructuralFeature getEcore_estructuralfeature() {
        return ecore_estructuralfeature;
    }

    public void setEcore_estructuralfeature(ecore_EStructuralFeature ecore_estructuralfeature) {
        this.ecore_estructuralfeature = ecore_estructuralfeature;
    }
    public ecore_EClassNotMatching getEcore_eclassnotmatching() {
        return ecore_eclassnotmatching;
    }

    public void setEcore_eclassnotmatching(ecore_EClassNotMatching ecore_eclassnotmatching) {
        this.ecore_eclassnotmatching = ecore_eclassnotmatching;
    }
    public List<ecore_EOperation> getEcore_eoperations() {
        return ecore_eoperations;
    }

    public void addEcore_eoperation(Ecore_eoperation ecore_eoperation) {
        this.ecore_eoperations.add(ecore_eoperation);
    }
    public ecore_EOperation getEcore_eoperation() {
        return ecore_eoperation;
    }

    public void setEcore_eoperation(ecore_EOperation ecore_eoperation) {
        this.ecore_eoperation = ecore_eoperation;
    }

}