





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEObject extends EObject {






    private List<ecoreDiff_EObject> ecorediff_eobjects;


    public ecoreDiff_ChangedEObject(
    ) {
        super(
        );
        this.ecorediff_eobjects = new ArrayList<>();
    }

    public ecoreDiff_ChangedEObject(
        ArrayList<ecoreDiff_EObject> ecorediff_eobjects    ) {
        this.ecorediff_eobjects = ecorediff_eobjects;
    }


    public List<ecoreDiff_EObject> getEcorediff_eobjects() {
        return ecorediff_eobjects;
    }

    public void addEcorediff_eobject(Ecorediff_eobject ecorediff_eobject) {
        this.ecorediff_eobjects.add(ecorediff_eobject);
    }

}