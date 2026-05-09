





import java.util.List;
import java.util.ArrayList;

public class ecore_EClass extends EClassifier {

    private boolean abstract;
    private boolean interface;





    private ecore_EOperation ecore_eoperation;




    private List<ecore_EStructuralFeature> ecore_estructuralfeatures;




    private List<ecore_EClass> ecore_eclasss;




    private List<ecore_EOperation> ecore_eoperations;




    private List<ecore_EOperation> ecore_eoperations;




    private List<ecore_EStructuralFeature> ecore_estructuralfeatures;




    private ecore_EStructuralFeature ecore_estructuralfeature;




    private List<ecore_EClass> ecore_eclasss;


    public ecore_EClass(
        boolean abstract,        boolean interface    ) {
        super(
        );
        this.abstract = abstract;
        this.interface = interface;
        this.ecore_estructuralfeatures = new ArrayList<>();
        this.ecore_eclasss = new ArrayList<>();
        this.ecore_eoperations = new ArrayList<>();
        this.ecore_eoperations = new ArrayList<>();
        this.ecore_estructuralfeatures = new ArrayList<>();
        this.ecore_eclasss = new ArrayList<>();
    }

    public ecore_EClass(
        boolean abstract,        boolean interface        ArrayList<ecore_EStructuralFeature> ecore_estructuralfeatures,        ArrayList<ecore_EClass> ecore_eclasss,        ArrayList<ecore_EOperation> ecore_eoperations,        ArrayList<ecore_EOperation> ecore_eoperations,        ArrayList<ecore_EStructuralFeature> ecore_estructuralfeatures,        ArrayList<ecore_EClass> ecore_eclasss    ) {
        this.abstract = abstract;
        this.interface = interface;
        this.ecore_estructuralfeatures = ecore_estructuralfeatures;
        this.ecore_eclasss = ecore_eclasss;
        this.ecore_eoperations = ecore_eoperations;
        this.ecore_eoperations = ecore_eoperations;
        this.ecore_estructuralfeatures = ecore_estructuralfeatures;
        this.ecore_eclasss = ecore_eclasss;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }

    public ecore_EOperation getEcore_eoperation() {
        return ecore_eoperation;
    }

    public void setEcore_eoperation(ecore_EOperation ecore_eoperation) {
        this.ecore_eoperation = ecore_eoperation;
    }
    public List<ecore_EStructuralFeature> getEcore_estructuralfeatures() {
        return ecore_estructuralfeatures;
    }

    public void addEcore_estructuralfeature(Ecore_estructuralfeature ecore_estructuralfeature) {
        this.ecore_estructuralfeatures.add(ecore_estructuralfeature);
    }
    public List<ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }
    public List<ecore_EOperation> getEcore_eoperations() {
        return ecore_eoperations;
    }

    public void addEcore_eoperation(Ecore_eoperation ecore_eoperation) {
        this.ecore_eoperations.add(ecore_eoperation);
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
    public ecore_EStructuralFeature getEcore_estructuralfeature() {
        return ecore_estructuralfeature;
    }

    public void setEcore_estructuralfeature(ecore_EStructuralFeature ecore_estructuralfeature) {
        this.ecore_estructuralfeature = ecore_estructuralfeature;
    }
    public List<ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }

}