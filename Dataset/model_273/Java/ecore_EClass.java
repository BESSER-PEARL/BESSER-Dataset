





import java.util.List;
import java.util.ArrayList;

public class ecore_EClass extends EClassifier {






    private List<ecore_EOperation> ecore_eoperations;




    private List<ecore_EStructuralFeature> ecore_estructuralfeatures;




    private List<ecore_EAttribute> ecore_eattributes;




    private List<ecore_EAttribute> ecore_eattributes;




    private List<ecore_EClass> ecore_eclasss;




    private List<ecore_EClass> ecore_eclasss;




    private List<ecore_EGenericType> ecore_egenerictypes;




    private List<ecore_EReference> ecore_ereferences;




    private ecore_EOperation ecore_eoperation;




    private ecore_EAttribute ecore_eattribute;




    private List<ecore_EGenericType> ecore_egenerictypes;




    private List<ecore_EReference> ecore_ereferences;




    private ecore_EReference ecore_ereference;




    private ecore_EStructuralFeature ecore_estructuralfeature;




    private List<ecore_EOperation> ecore_eoperations;




    private List<ecore_EReference> ecore_ereferences;




    private List<ecore_EStructuralFeature> ecore_estructuralfeatures;


    public ecore_EClass(
    ) {
        super(
        );
        this.ecore_eoperations = new ArrayList<>();
        this.ecore_estructuralfeatures = new ArrayList<>();
        this.ecore_eattributes = new ArrayList<>();
        this.ecore_eattributes = new ArrayList<>();
        this.ecore_eclasss = new ArrayList<>();
        this.ecore_eclasss = new ArrayList<>();
        this.ecore_egenerictypes = new ArrayList<>();
        this.ecore_ereferences = new ArrayList<>();
        this.ecore_egenerictypes = new ArrayList<>();
        this.ecore_ereferences = new ArrayList<>();
        this.ecore_eoperations = new ArrayList<>();
        this.ecore_ereferences = new ArrayList<>();
        this.ecore_estructuralfeatures = new ArrayList<>();
    }

    public ecore_EClass(
        ArrayList<ecore_EOperation> ecore_eoperations,        ArrayList<ecore_EStructuralFeature> ecore_estructuralfeatures,        ArrayList<ecore_EAttribute> ecore_eattributes,        ArrayList<ecore_EAttribute> ecore_eattributes,        ArrayList<ecore_EClass> ecore_eclasss,        ArrayList<ecore_EClass> ecore_eclasss,        ArrayList<ecore_EGenericType> ecore_egenerictypes,        ArrayList<ecore_EReference> ecore_ereferences,        ArrayList<ecore_EGenericType> ecore_egenerictypes,        ArrayList<ecore_EReference> ecore_ereferences,        ArrayList<ecore_EOperation> ecore_eoperations,        ArrayList<ecore_EReference> ecore_ereferences,        ArrayList<ecore_EStructuralFeature> ecore_estructuralfeatures    ) {
        this.ecore_eoperations = ecore_eoperations;
        this.ecore_estructuralfeatures = ecore_estructuralfeatures;
        this.ecore_eattributes = ecore_eattributes;
        this.ecore_eattributes = ecore_eattributes;
        this.ecore_eclasss = ecore_eclasss;
        this.ecore_eclasss = ecore_eclasss;
        this.ecore_egenerictypes = ecore_egenerictypes;
        this.ecore_ereferences = ecore_ereferences;
        this.ecore_egenerictypes = ecore_egenerictypes;
        this.ecore_ereferences = ecore_ereferences;
        this.ecore_eoperations = ecore_eoperations;
        this.ecore_ereferences = ecore_ereferences;
        this.ecore_estructuralfeatures = ecore_estructuralfeatures;
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
    public List<ecore_EAttribute> getEcore_eattributes() {
        return ecore_eattributes;
    }

    public void addEcore_eattribute(Ecore_eattribute ecore_eattribute) {
        this.ecore_eattributes.add(ecore_eattribute);
    }
    public List<ecore_EAttribute> getEcore_eattributes() {
        return ecore_eattributes;
    }

    public void addEcore_eattribute(Ecore_eattribute ecore_eattribute) {
        this.ecore_eattributes.add(ecore_eattribute);
    }
    public List<ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }
    public List<ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }
    public List<ecore_EGenericType> getEcore_egenerictypes() {
        return ecore_egenerictypes;
    }

    public void addEcore_egenerictype(Ecore_egenerictype ecore_egenerictype) {
        this.ecore_egenerictypes.add(ecore_egenerictype);
    }
    public List<ecore_EReference> getEcore_ereferences() {
        return ecore_ereferences;
    }

    public void addEcore_ereference(Ecore_ereference ecore_ereference) {
        this.ecore_ereferences.add(ecore_ereference);
    }
    public ecore_EOperation getEcore_eoperation() {
        return ecore_eoperation;
    }

    public void setEcore_eoperation(ecore_EOperation ecore_eoperation) {
        this.ecore_eoperation = ecore_eoperation;
    }
    public ecore_EAttribute getEcore_eattribute() {
        return ecore_eattribute;
    }

    public void setEcore_eattribute(ecore_EAttribute ecore_eattribute) {
        this.ecore_eattribute = ecore_eattribute;
    }
    public List<ecore_EGenericType> getEcore_egenerictypes() {
        return ecore_egenerictypes;
    }

    public void addEcore_egenerictype(Ecore_egenerictype ecore_egenerictype) {
        this.ecore_egenerictypes.add(ecore_egenerictype);
    }
    public List<ecore_EReference> getEcore_ereferences() {
        return ecore_ereferences;
    }

    public void addEcore_ereference(Ecore_ereference ecore_ereference) {
        this.ecore_ereferences.add(ecore_ereference);
    }
    public ecore_EReference getEcore_ereference() {
        return ecore_ereference;
    }

    public void setEcore_ereference(ecore_EReference ecore_ereference) {
        this.ecore_ereference = ecore_ereference;
    }
    public ecore_EStructuralFeature getEcore_estructuralfeature() {
        return ecore_estructuralfeature;
    }

    public void setEcore_estructuralfeature(ecore_EStructuralFeature ecore_estructuralfeature) {
        this.ecore_estructuralfeature = ecore_estructuralfeature;
    }
    public List<ecore_EOperation> getEcore_eoperations() {
        return ecore_eoperations;
    }

    public void addEcore_eoperation(Ecore_eoperation ecore_eoperation) {
        this.ecore_eoperations.add(ecore_eoperation);
    }
    public List<ecore_EReference> getEcore_ereferences() {
        return ecore_ereferences;
    }

    public void addEcore_ereference(Ecore_ereference ecore_ereference) {
        this.ecore_ereferences.add(ecore_ereference);
    }
    public List<ecore_EStructuralFeature> getEcore_estructuralfeatures() {
        return ecore_estructuralfeatures;
    }

    public void addEcore_estructuralfeature(Ecore_estructuralfeature ecore_estructuralfeature) {
        this.ecore_estructuralfeatures.add(ecore_estructuralfeature);
    }

}