





import java.util.List;
import java.util.ArrayList;

public class ecore_EClass extends EClassifier {

    private boolean interface;
    private boolean abstract;





    private List<ecore_EAttribute> ecore_eattributes;




    private List<ecore_EAttribute> ecore_eattributes;




    private List<ecore_EReference> ecore_ereferences;




    private ecore_EClass ecore_eclass;




    private List<ecore_EClass> ecore_eclasss;




    private ecore_EReference ecore_ereference;




    private List<ecore_EReference> ecore_ereferences;




    private List<ecore_EReference> ecore_ereferences;




    private ecore_EAttribute ecore_eattribute;


    public ecore_EClass(
        boolean interface,        boolean abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.ecore_eattributes = new ArrayList<>();
        this.ecore_eattributes = new ArrayList<>();
        this.ecore_ereferences = new ArrayList<>();
        this.ecore_eclasss = new ArrayList<>();
        this.ecore_ereferences = new ArrayList<>();
        this.ecore_ereferences = new ArrayList<>();
    }

    public ecore_EClass(
        boolean interface,        boolean abstract        ArrayList<ecore_EAttribute> ecore_eattributes,        ArrayList<ecore_EAttribute> ecore_eattributes,        ArrayList<ecore_EReference> ecore_ereferences,        ArrayList<ecore_EClass> ecore_eclasss,        ArrayList<ecore_EReference> ecore_ereferences,        ArrayList<ecore_EReference> ecore_ereferences    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.ecore_eattributes = ecore_eattributes;
        this.ecore_eattributes = ecore_eattributes;
        this.ecore_ereferences = ecore_ereferences;
        this.ecore_eclasss = ecore_eclasss;
        this.ecore_ereferences = ecore_ereferences;
        this.ecore_ereferences = ecore_ereferences;
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
    public List<ecore_EReference> getEcore_ereferences() {
        return ecore_ereferences;
    }

    public void addEcore_ereference(Ecore_ereference ecore_ereference) {
        this.ecore_ereferences.add(ecore_ereference);
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public List<ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }
    public ecore_EReference getEcore_ereference() {
        return ecore_ereference;
    }

    public void setEcore_ereference(ecore_EReference ecore_ereference) {
        this.ecore_ereference = ecore_ereference;
    }
    public List<ecore_EReference> getEcore_ereferences() {
        return ecore_ereferences;
    }

    public void addEcore_ereference(Ecore_ereference ecore_ereference) {
        this.ecore_ereferences.add(ecore_ereference);
    }
    public List<ecore_EReference> getEcore_ereferences() {
        return ecore_ereferences;
    }

    public void addEcore_ereference(Ecore_ereference ecore_ereference) {
        this.ecore_ereferences.add(ecore_ereference);
    }
    public ecore_EAttribute getEcore_eattribute() {
        return ecore_eattribute;
    }

    public void setEcore_eattribute(ecore_EAttribute ecore_eattribute) {
        this.ecore_eattribute = ecore_eattribute;
    }

}