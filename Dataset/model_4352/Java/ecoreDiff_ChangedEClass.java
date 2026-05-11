





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEClass extends EClass {






    private ecoreDiff_EObject ecorediff_eobject;




    private List<ecoreDiff_EClass> ecorediff_eclasss;


    public ecoreDiff_ChangedEClass(
    ) {
        super(
        );
        this.ecorediff_eclasss = new ArrayList<>();
    }

    public ecoreDiff_ChangedEClass(
        ArrayList<ecoreDiff_EClass> ecorediff_eclasss    ) {
        this.ecorediff_eclasss = ecorediff_eclasss;
    }


    public ecoreDiff_EObject getEcorediff_eobject() {
        return ecorediff_eobject;
    }

    public void setEcorediff_eobject(ecoreDiff_EObject ecorediff_eobject) {
        this.ecorediff_eobject = ecorediff_eobject;
    }
    public List<ecoreDiff_EClass> getEcorediff_eclasss() {
        return ecorediff_eclasss;
    }

    public void addEcorediff_eclass(Ecorediff_eclass ecorediff_eclass) {
        this.ecorediff_eclasss.add(ecorediff_eclass);
    }

}