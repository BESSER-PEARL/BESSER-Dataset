





import java.util.List;
import java.util.ArrayList;

public class ecore_EClass extends EClassifier {

    private boolean abstract;
    private boolean interface;





    private List<ecore_EClass> ecore_eclasss;


    public ecore_EClass(
        boolean abstract,        boolean interface    ) {
        super(
        );
        this.abstract = abstract;
        this.interface = interface;
        this.ecore_eclasss = new ArrayList<>();
    }

    public ecore_EClass(
        boolean abstract,        boolean interface        ArrayList<ecore_EClass> ecore_eclasss    ) {
        this.abstract = abstract;
        this.interface = interface;
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

    public List<ecore_EClass> getEcore_eclasss() {
        return ecore_eclasss;
    }

    public void addEcore_eclass(Ecore_eclass ecore_eclass) {
        this.ecore_eclasss.add(ecore_eclass);
    }

}