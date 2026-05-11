





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEOperation extends EOperation {






    private List<ecoreDiff_EOperation> ecorediff_eoperations;


    public ecoreDiff_ChangedEOperation(
    ) {
        super(
        );
        this.ecorediff_eoperations = new ArrayList<>();
    }

    public ecoreDiff_ChangedEOperation(
        ArrayList<ecoreDiff_EOperation> ecorediff_eoperations    ) {
        this.ecorediff_eoperations = ecorediff_eoperations;
    }


    public List<ecoreDiff_EOperation> getEcorediff_eoperations() {
        return ecorediff_eoperations;
    }

    public void addEcorediff_eoperation(Ecorediff_eoperation ecorediff_eoperation) {
        this.ecorediff_eoperations.add(ecorediff_eoperation);
    }

}