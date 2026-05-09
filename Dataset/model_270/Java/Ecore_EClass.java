





import java.util.List;
import java.util.ArrayList;

public class Ecore_EClass extends EClassifier {

    private boolean abstract;
    private boolean interface;





    private List<Ecore_EReference> ecore_ereferences;




    private Ecore_EReference ecore_ereference;




    private List<Ecore_EAttribute> ecore_eattributes;




    private List<Ecore_EClass> ecore_eclasss;




    private List<Ecore_EClass> ecore_eclasss;




    private Ecore_EAttribute ecore_eattribute;




    private List<Ecore_EAttribute> ecore_eattributes;




    private List<Ecore_EReference> ecore_ereferences;




    private List<Ecore_EReference> ecore_ereferences;


    public Ecore_EClass(
        boolean abstract,        boolean interface    ) {
        super(
        );
        this.abstract = abstract;
        this.interface = interface;
        this.ecore_ereferences = new ArrayList<>();
        this.ecore_eattributes = new ArrayList<>();
        this.ecore_eclasss = new ArrayList<>();
        this.ecore_eclasss = new ArrayList<>();
        this.ecore_eattributes = new ArrayList<>();
        this.ecore_ereferences = new ArrayList<>();
        this.ecore_ereferences = new ArrayList<>();
    }

    public Ecore_EClass(
        boolean abstract,        boolean interface        ArrayList<Ecore_EReference> ecore_ereferences,        ArrayList<Ecore_EAttribute> ecore_eattributes,        ArrayList<Ecore_EClass> ecore_eclasss,        ArrayList<Ecore_EClass> ecore_eclasss,        ArrayList<Ecore_EAttribute> ecore_eattributes,        ArrayList<Ecore_EReference> ecore_ereferences,        ArrayList<Ecore_EReference> ecore_ereferences    ) {
        this.abstract = abstract;
        this.interface = interface;
        this.ecore_ereferences = ecore_ereferences;
        this.ecore_eattributes = ecore_eattributes;
        this.ecore_eclasss = ecore_eclasss;
        this.ecore_eclasss = ecore_eclasss;
        this.ecore_eattributes = ecore_eattributes;
        this.ecore_ereferences = ecore_ereferences;
        this.ecore_ereferences = ecore_ereferences;
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

    public List<Ecore_EReference> getEcore_ereferences() {
        return ecore_ereferences;
    }

    public void addEcore_ereference(Ecore_ereference ecore_ereference) {
        this.ecore_ereferences.add(ecore_ereference);
    }
    public Ecore_EReference getEcore_ereference() {
        return ecore_ereference;
    }

    public void setEcore_ereference(Ecore_EReference ecore_ereference) {
        this.ecore_ereference = ecore_ereference;
    }
    public List<Ecore_EAttribute> getEcore_eattributes() {
        return ecore_eattributes;
    }

    public void addEcore_eattribute(Ecore_eattribute ecore_eattribute) {
        this.ecore_eattributes.add(ecore_eattribute);
    }
    public List<Ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }
    public List<Ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }
    public Ecore_EAttribute getEcore_eattribute() {
        return ecore_eattribute;
    }

    public void setEcore_eattribute(Ecore_EAttribute ecore_eattribute) {
        this.ecore_eattribute = ecore_eattribute;
    }
    public List<Ecore_EAttribute> getEcore_eattributes() {
        return ecore_eattributes;
    }

    public void addEcore_eattribute(Ecore_eattribute ecore_eattribute) {
        this.ecore_eattributes.add(ecore_eattribute);
    }
    public List<Ecore_EReference> getEcore_ereferences() {
        return ecore_ereferences;
    }

    public void addEcore_ereference(Ecore_ereference ecore_ereference) {
        this.ecore_ereferences.add(ecore_ereference);
    }
    public List<Ecore_EReference> getEcore_ereferences() {
        return ecore_ereferences;
    }

    public void addEcore_ereference(Ecore_ereference ecore_ereference) {
        this.ecore_ereferences.add(ecore_ereference);
    }

}