





import java.util.List;
import java.util.ArrayList;

public class ecore_EClass extends EClassifier {

    private boolean interface;
    private boolean abstract;





    private List<ecore_EClass> ecore_eclasss;




    private ecore_EClass ecore_eclass;


    public ecore_EClass(
        boolean interface,        boolean abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.ecore_eclasss = new ArrayList<>();
    }

    public ecore_EClass(
        boolean interface,        boolean abstract        ArrayList<ecore_EClass> ecore_eclasss    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.ecore_eclasss = ecore_eclasss;
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

    public List<ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }

}