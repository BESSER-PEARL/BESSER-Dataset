





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EClass extends EClassifier {

    private boolean interface;
    private boolean abstract;





    private ecoreDiff_EClass ecorediff_eclass;




    private List<ecoreDiff_EClass> ecorediff_eclasss;


    public ecoreDiff_EClass(
        boolean interface,        boolean abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.ecorediff_eclasss = new ArrayList<>();
    }

    public ecoreDiff_EClass(
        boolean interface,        boolean abstract        ArrayList<ecoreDiff_EClass> ecorediff_eclasss    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.ecorediff_eclasss = ecorediff_eclasss;
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

    public ecoreDiff_EClass getEcorediff_eclass() {
        return ecorediff_eclass;
    }

    public void setEcorediff_eclass(ecoreDiff_EClass ecorediff_eclass) {
        this.ecorediff_eclass = ecorediff_eclass;
    }
    public List<ecoreDiff_EClass> getEcorediff_eclasss() {
        return ecorediff_eclasss;
    }

    public void addEcorediff_eclass(Ecorediff_eclass ecorediff_eclass) {
        this.ecorediff_eclasss.add(ecorediff_eclass);
    }

}