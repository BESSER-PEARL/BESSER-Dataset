





import java.util.List;
import java.util.ArrayList;

public class ecorer_EClass extends EClassifier {

    private boolean interface;
    private boolean abstract;





    private List<ecorer_EReference> ecorer_ereferences;




    private List<ecorer_EOperation> ecorer_eoperations;




    private List<ecorer_EReference> ecorer_ereferences;




    private List<ecorer_EAttribute> ecorer_eattributes;




    private ecorer_EReference ecorer_ereference;




    private List<ecorer_EClass> ecorer_eclasss;




    private ecorer_EClass ecorer_eclass;




    private List<ecorer_EReference> ecorer_ereferences;




    private List<ecorer_EAttribute> ecorer_eattributes;




    private ecorer_EAttribute ecorer_eattribute;




    private List<ecorer_EOperation> ecorer_eoperations;




    private ecorer_EOperation ecorer_eoperation;


    public ecorer_EClass(
        boolean interface,        boolean abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.ecorer_ereferences = new ArrayList<>();
        this.ecorer_eoperations = new ArrayList<>();
        this.ecorer_ereferences = new ArrayList<>();
        this.ecorer_eattributes = new ArrayList<>();
        this.ecorer_eclasss = new ArrayList<>();
        this.ecorer_ereferences = new ArrayList<>();
        this.ecorer_eattributes = new ArrayList<>();
        this.ecorer_eoperations = new ArrayList<>();
    }

    public ecorer_EClass(
        boolean interface,        boolean abstract        ArrayList<ecorer_EReference> ecorer_ereferences,        ArrayList<ecorer_EOperation> ecorer_eoperations,        ArrayList<ecorer_EReference> ecorer_ereferences,        ArrayList<ecorer_EAttribute> ecorer_eattributes,        ArrayList<ecorer_EClass> ecorer_eclasss,        ArrayList<ecorer_EReference> ecorer_ereferences,        ArrayList<ecorer_EAttribute> ecorer_eattributes,        ArrayList<ecorer_EOperation> ecorer_eoperations    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.ecorer_ereferences = ecorer_ereferences;
        this.ecorer_eoperations = ecorer_eoperations;
        this.ecorer_ereferences = ecorer_ereferences;
        this.ecorer_eattributes = ecorer_eattributes;
        this.ecorer_eclasss = ecorer_eclasss;
        this.ecorer_ereferences = ecorer_ereferences;
        this.ecorer_eattributes = ecorer_eattributes;
        this.ecorer_eoperations = ecorer_eoperations;
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

    public List<ecorer_EReference> getEcorer_ereferences() {
        return ecorer_ereferences;
    }

    public void addEcorer_ereference(Ecorer_ereference ecorer_ereference) {
        this.ecorer_ereferences.add(ecorer_ereference);
    }
    public List<ecorer_EOperation> getEcorer_eoperations() {
        return ecorer_eoperations;
    }

    public void addEcorer_eoperation(Ecorer_eoperation ecorer_eoperation) {
        this.ecorer_eoperations.add(ecorer_eoperation);
    }
    public List<ecorer_EReference> getEcorer_ereferences() {
        return ecorer_ereferences;
    }

    public void addEcorer_ereference(Ecorer_ereference ecorer_ereference) {
        this.ecorer_ereferences.add(ecorer_ereference);
    }
    public List<ecorer_EAttribute> getEcorer_eattributes() {
        return ecorer_eattributes;
    }

    public void addEcorer_eattribute(Ecorer_eattribute ecorer_eattribute) {
        this.ecorer_eattributes.add(ecorer_eattribute);
    }
    public ecorer_EReference getEcorer_ereference() {
        return ecorer_ereference;
    }

    public void setEcorer_ereference(ecorer_EReference ecorer_ereference) {
        this.ecorer_ereference = ecorer_ereference;
    }
    public List<ecorer_EClass> getEcorer_eclasss() {
        return ecorer_eclasss;
    }

    public void addEcorer_eclass(Ecorer_eclass ecorer_eclass) {
        this.ecorer_eclasss.add(ecorer_eclass);
    }
    public ecorer_EClass getEcorer_eclass() {
        return ecorer_eclass;
    }

    public void setEcorer_eclass(ecorer_EClass ecorer_eclass) {
        this.ecorer_eclass = ecorer_eclass;
    }
    public List<ecorer_EReference> getEcorer_ereferences() {
        return ecorer_ereferences;
    }

    public void addEcorer_ereference(Ecorer_ereference ecorer_ereference) {
        this.ecorer_ereferences.add(ecorer_ereference);
    }
    public List<ecorer_EAttribute> getEcorer_eattributes() {
        return ecorer_eattributes;
    }

    public void addEcorer_eattribute(Ecorer_eattribute ecorer_eattribute) {
        this.ecorer_eattributes.add(ecorer_eattribute);
    }
    public ecorer_EAttribute getEcorer_eattribute() {
        return ecorer_eattribute;
    }

    public void setEcorer_eattribute(ecorer_EAttribute ecorer_eattribute) {
        this.ecorer_eattribute = ecorer_eattribute;
    }
    public List<ecorer_EOperation> getEcorer_eoperations() {
        return ecorer_eoperations;
    }

    public void addEcorer_eoperation(Ecorer_eoperation ecorer_eoperation) {
        this.ecorer_eoperations.add(ecorer_eoperation);
    }
    public ecorer_EOperation getEcorer_eoperation() {
        return ecorer_eoperation;
    }

    public void setEcorer_eoperation(ecorer_EOperation ecorer_eoperation) {
        this.ecorer_eoperation = ecorer_eoperation;
    }

}