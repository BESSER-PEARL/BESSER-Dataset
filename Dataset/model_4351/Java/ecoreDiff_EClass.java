





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EClass extends EClassifier {

    private boolean abstract;
    private boolean interface;





    private ecoreDiff_EClass ecorediff_eclass;




    private List<ecoreDiff_EClass> ecorediff_eclasss;


    public ecoreDiff_EClass(
        boolean abstract,        boolean interface    ) {
        super(
        );
        this.abstract = abstract;
        this.interface = interface;
        this.ecorediff_eclasss = new ArrayList<>();
    }

    public ecoreDiff_EClass(
        boolean abstract,        boolean interface        ArrayList<ecoreDiff_EClass> ecorediff_eclasss    ) {
        this.abstract = abstract;
        this.interface = interface;
        this.ecorediff_eclasss = ecorediff_eclasss;
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