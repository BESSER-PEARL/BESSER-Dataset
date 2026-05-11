





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEDataType extends EDataType {






    private List<ecoreDiff_EDataType> ecorediff_edatatypes;


    public ecoreDiff_ChangedEDataType(
    ) {
        super(
        );
        this.ecorediff_edatatypes = new ArrayList<>();
    }

    public ecoreDiff_ChangedEDataType(
        ArrayList<ecoreDiff_EDataType> ecorediff_edatatypes    ) {
        this.ecorediff_edatatypes = ecorediff_edatatypes;
    }


    public List<ecoreDiff_EDataType> getEcorediff_edatatypes() {
        return ecorediff_edatatypes;
    }

    public void addEcorediff_edatatype(Ecorediff_edatatype ecorediff_edatatype) {
        this.ecorediff_edatatypes.add(ecorediff_edatatype);
    }

}