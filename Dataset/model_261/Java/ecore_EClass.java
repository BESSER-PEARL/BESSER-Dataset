





import java.util.List;
import java.util.ArrayList;

public class ecore_EClass extends EClassifier {

    private boolean interface;
    private boolean abstract;





    private List<ecore_EAttribute> ecore_eattributes;




    private ecore_EAttribute ecore_eattribute;




    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;




    private List<ecore_EAttribute> ecore_eattributes;


    public ecore_EClass(
        boolean interface,        boolean abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.ecore_eattributes = new ArrayList<>();
        this.ecore_eattributes = new ArrayList<>();
    }

    public ecore_EClass(
        boolean interface,        boolean abstract        ArrayList<ecore_EAttribute> ecore_eattributes,        ArrayList<ecore_EAttribute> ecore_eattributes    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.ecore_eattributes = ecore_eattributes;
        this.ecore_eattributes = ecore_eattributes;
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
    public ecore_EAttribute getEcore_eattribute() {
        return ecore_eattribute;
    }

    public void setEcore_eattribute(ecore_EAttribute ecore_eattribute) {
        this.ecore_eattribute = ecore_eattribute;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public List<ecore_EAttribute> getEcore_eattributes() {
        return ecore_eattributes;
    }

    public void addEcore_eattribute(Ecore_eattribute ecore_eattribute) {
        this.ecore_eattributes.add(ecore_eattribute);
    }

}