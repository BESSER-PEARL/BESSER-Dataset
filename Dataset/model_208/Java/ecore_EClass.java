





import java.util.List;
import java.util.ArrayList;

public class ecore_EClass extends EClassifier {

    private String interface;
    private String abstract;





    private List<EAttribute> eattributes;




    private List<EStructuralFeature> estructuralfeatures;




    private EAttribute eattribute;




    private List<EClass> eclasss;




    private List<EClass> eclasss;




    private List<EReference> ereferences;




    private List<EStructuralFeature> estructuralfeatures;




    private List<EReference> ereferences;




    private List<EAttribute> eattributes;




    private List<EReference> ereferences;




    private List<EOperation> eoperations;




    private List<EOperation> eoperations;


    public ecore_EClass(
        String interface,        String abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.eattributes = new ArrayList<>();
        this.estructuralfeatures = new ArrayList<>();
        this.eclasss = new ArrayList<>();
        this.eclasss = new ArrayList<>();
        this.ereferences = new ArrayList<>();
        this.estructuralfeatures = new ArrayList<>();
        this.ereferences = new ArrayList<>();
        this.eattributes = new ArrayList<>();
        this.ereferences = new ArrayList<>();
        this.eoperations = new ArrayList<>();
        this.eoperations = new ArrayList<>();
    }

    public ecore_EClass(
        String interface,        String abstract        ArrayList<EAttribute> eattributes,        ArrayList<EStructuralFeature> estructuralfeatures,        ArrayList<EClass> eclasss,        ArrayList<EClass> eclasss,        ArrayList<EReference> ereferences,        ArrayList<EStructuralFeature> estructuralfeatures,        ArrayList<EReference> ereferences,        ArrayList<EAttribute> eattributes,        ArrayList<EReference> ereferences,        ArrayList<EOperation> eoperations,        ArrayList<EOperation> eoperations    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.eattributes = eattributes;
        this.estructuralfeatures = estructuralfeatures;
        this.eclasss = eclasss;
        this.eclasss = eclasss;
        this.ereferences = ereferences;
        this.estructuralfeatures = estructuralfeatures;
        this.ereferences = ereferences;
        this.eattributes = eattributes;
        this.ereferences = ereferences;
        this.eoperations = eoperations;
        this.eoperations = eoperations;
    }

    public String getInterface() {
        return interface;
    }

    public void setInterface(String interface) {
        this.interface = interface;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }

    public List<EAttribute> getEattributes() {
        return eattributes;
    }

    public void addEattribute(Eattribute eattribute) {
        this.eattributes.add(eattribute);
    }
    public List<EStructuralFeature> getEstructuralfeatures() {
        return estructuralfeatures;
    }

    public void addEstructuralfeature(Estructuralfeature estructuralfeature) {
        this.estructuralfeatures.add(estructuralfeature);
    }
    public EAttribute getEattribute() {
        return eattribute;
    }

    public void setEattribute(EAttribute eattribute) {
        this.eattribute = eattribute;
    }
    public List<EClass> getEclasss() {
        return eclasss;
    }

    public void addEclass(Eclass eclass) {
        this.eclasss.add(eclass);
    }
    public List<EClass> getEclasss() {
        return eclasss;
    }

    public void addEclass(Eclass eclass) {
        this.eclasss.add(eclass);
    }
    public List<EReference> getEreferences() {
        return ereferences;
    }

    public void addEreference(Ereference ereference) {
        this.ereferences.add(ereference);
    }
    public List<EStructuralFeature> getEstructuralfeatures() {
        return estructuralfeatures;
    }

    public void addEstructuralfeature(Estructuralfeature estructuralfeature) {
        this.estructuralfeatures.add(estructuralfeature);
    }
    public List<EReference> getEreferences() {
        return ereferences;
    }

    public void addEreference(Ereference ereference) {
        this.ereferences.add(ereference);
    }
    public List<EAttribute> getEattributes() {
        return eattributes;
    }

    public void addEattribute(Eattribute eattribute) {
        this.eattributes.add(eattribute);
    }
    public List<EReference> getEreferences() {
        return ereferences;
    }

    public void addEreference(Ereference ereference) {
        this.ereferences.add(ereference);
    }
    public List<EOperation> getEoperations() {
        return eoperations;
    }

    public void addEoperation(Eoperation eoperation) {
        this.eoperations.add(eoperation);
    }
    public List<EOperation> getEoperations() {
        return eoperations;
    }

    public void addEoperation(Eoperation eoperation) {
        this.eoperations.add(eoperation);
    }

}