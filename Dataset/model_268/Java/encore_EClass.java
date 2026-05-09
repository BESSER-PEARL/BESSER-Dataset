





import java.util.List;
import java.util.ArrayList;

public class encore_EClass extends EClassifier {

    private boolean interface;
    private boolean abstract;





    private List<encore_EReference> encore_ereferences;




    private List<encore_EAttribute> encore_eattributes;




    private List<encore_EGenericType> encore_egenerictypes;




    private List<encore_EReference> encore_ereferences;




    private List<encore_EReference> encore_ereferences;




    private List<encore_EClass> encore_eclasss;




    private encore_EOperation encore_eoperation;




    private encore_EStructuralFeature encore_estructuralfeature;




    private List<encore_EClass> encore_eclasss;




    private List<encore_EOperation> encore_eoperations;




    private List<encore_EStructuralFeature> encore_estructuralfeatures;




    private List<encore_EStructuralFeature> encore_estructuralfeatures;




    private encore_EReference encore_ereference;




    private List<encore_EOperation> encore_eoperations;




    private List<encore_EGenericType> encore_egenerictypes;




    private encore_EAttribute encore_eattribute;




    private List<encore_EAttribute> encore_eattributes;


    public encore_EClass(
        boolean interface,        boolean abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.encore_ereferences = new ArrayList<>();
        this.encore_eattributes = new ArrayList<>();
        this.encore_egenerictypes = new ArrayList<>();
        this.encore_ereferences = new ArrayList<>();
        this.encore_ereferences = new ArrayList<>();
        this.encore_eclasss = new ArrayList<>();
        this.encore_eclasss = new ArrayList<>();
        this.encore_eoperations = new ArrayList<>();
        this.encore_estructuralfeatures = new ArrayList<>();
        this.encore_estructuralfeatures = new ArrayList<>();
        this.encore_eoperations = new ArrayList<>();
        this.encore_egenerictypes = new ArrayList<>();
        this.encore_eattributes = new ArrayList<>();
    }

    public encore_EClass(
        boolean interface,        boolean abstract        ArrayList<encore_EReference> encore_ereferences,        ArrayList<encore_EAttribute> encore_eattributes,        ArrayList<encore_EGenericType> encore_egenerictypes,        ArrayList<encore_EReference> encore_ereferences,        ArrayList<encore_EReference> encore_ereferences,        ArrayList<encore_EClass> encore_eclasss,        ArrayList<encore_EClass> encore_eclasss,        ArrayList<encore_EOperation> encore_eoperations,        ArrayList<encore_EStructuralFeature> encore_estructuralfeatures,        ArrayList<encore_EStructuralFeature> encore_estructuralfeatures,        ArrayList<encore_EOperation> encore_eoperations,        ArrayList<encore_EGenericType> encore_egenerictypes,        ArrayList<encore_EAttribute> encore_eattributes    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.encore_ereferences = encore_ereferences;
        this.encore_eattributes = encore_eattributes;
        this.encore_egenerictypes = encore_egenerictypes;
        this.encore_ereferences = encore_ereferences;
        this.encore_ereferences = encore_ereferences;
        this.encore_eclasss = encore_eclasss;
        this.encore_eclasss = encore_eclasss;
        this.encore_eoperations = encore_eoperations;
        this.encore_estructuralfeatures = encore_estructuralfeatures;
        this.encore_estructuralfeatures = encore_estructuralfeatures;
        this.encore_eoperations = encore_eoperations;
        this.encore_egenerictypes = encore_egenerictypes;
        this.encore_eattributes = encore_eattributes;
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

    public List<encore_EReference> getEncore_ereferences() {
        return encore_ereferences;
    }

    public void addEncore_ereference(Encore_ereference encore_ereference) {
        this.encore_ereferences.add(encore_ereference);
    }
    public List<encore_EAttribute> getEncore_eattributes() {
        return encore_eattributes;
    }

    public void addEncore_eattribute(Encore_eattribute encore_eattribute) {
        this.encore_eattributes.add(encore_eattribute);
    }
    public List<encore_EGenericType> getEncore_egenerictypes() {
        return encore_egenerictypes;
    }

    public void addEncore_egenerictype(Encore_egenerictype encore_egenerictype) {
        this.encore_egenerictypes.add(encore_egenerictype);
    }
    public List<encore_EReference> getEncore_ereferences() {
        return encore_ereferences;
    }

    public void addEncore_ereference(Encore_ereference encore_ereference) {
        this.encore_ereferences.add(encore_ereference);
    }
    public List<encore_EReference> getEncore_ereferences() {
        return encore_ereferences;
    }

    public void addEncore_ereference(Encore_ereference encore_ereference) {
        this.encore_ereferences.add(encore_ereference);
    }
    public List<encore_EClass> getEncore_eclasss() {
        return encore_eclasss;
    }

    public void addEncore_eclass(Encore_eclass encore_eclass) {
        this.encore_eclasss.add(encore_eclass);
    }
    public encore_EOperation getEncore_eoperation() {
        return encore_eoperation;
    }

    public void setEncore_eoperation(encore_EOperation encore_eoperation) {
        this.encore_eoperation = encore_eoperation;
    }
    public encore_EStructuralFeature getEncore_estructuralfeature() {
        return encore_estructuralfeature;
    }

    public void setEncore_estructuralfeature(encore_EStructuralFeature encore_estructuralfeature) {
        this.encore_estructuralfeature = encore_estructuralfeature;
    }
    public List<encore_EClass> getEncore_eclasss() {
        return encore_eclasss;
    }

    public void addEncore_eclass(Encore_eclass encore_eclass) {
        this.encore_eclasss.add(encore_eclass);
    }
    public List<encore_EOperation> getEncore_eoperations() {
        return encore_eoperations;
    }

    public void addEncore_eoperation(Encore_eoperation encore_eoperation) {
        this.encore_eoperations.add(encore_eoperation);
    }
    public List<encore_EStructuralFeature> getEncore_estructuralfeatures() {
        return encore_estructuralfeatures;
    }

    public void addEncore_estructuralfeature(Encore_estructuralfeature encore_estructuralfeature) {
        this.encore_estructuralfeatures.add(encore_estructuralfeature);
    }
    public List<encore_EStructuralFeature> getEncore_estructuralfeatures() {
        return encore_estructuralfeatures;
    }

    public void addEncore_estructuralfeature(Encore_estructuralfeature encore_estructuralfeature) {
        this.encore_estructuralfeatures.add(encore_estructuralfeature);
    }
    public encore_EReference getEncore_ereference() {
        return encore_ereference;
    }

    public void setEncore_ereference(encore_EReference encore_ereference) {
        this.encore_ereference = encore_ereference;
    }
    public List<encore_EOperation> getEncore_eoperations() {
        return encore_eoperations;
    }

    public void addEncore_eoperation(Encore_eoperation encore_eoperation) {
        this.encore_eoperations.add(encore_eoperation);
    }
    public List<encore_EGenericType> getEncore_egenerictypes() {
        return encore_egenerictypes;
    }

    public void addEncore_egenerictype(Encore_egenerictype encore_egenerictype) {
        this.encore_egenerictypes.add(encore_egenerictype);
    }
    public encore_EAttribute getEncore_eattribute() {
        return encore_eattribute;
    }

    public void setEncore_eattribute(encore_EAttribute encore_eattribute) {
        this.encore_eattribute = encore_eattribute;
    }
    public List<encore_EAttribute> getEncore_eattributes() {
        return encore_eattributes;
    }

    public void addEncore_eattribute(Encore_eattribute encore_eattribute) {
        this.encore_eattributes.add(encore_eattribute);
    }

}