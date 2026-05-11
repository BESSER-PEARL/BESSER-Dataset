





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEGenericType extends EGenericType {






    private List<ecoreDiff_EGenericType> ecorediff_egenerictypes;


    public ecoreDiff_ChangedEGenericType(
    ) {
        super(
        );
        this.ecorediff_egenerictypes = new ArrayList<>();
    }

    public ecoreDiff_ChangedEGenericType(
        ArrayList<ecoreDiff_EGenericType> ecorediff_egenerictypes    ) {
        this.ecorediff_egenerictypes = ecorediff_egenerictypes;
    }


    public List<ecoreDiff_EGenericType> getEcorediff_egenerictypes() {
        return ecorediff_egenerictypes;
    }

    public void addEcorediff_egenerictype(Ecorediff_egenerictype ecorediff_egenerictype) {
        this.ecorediff_egenerictypes.add(ecorediff_egenerictype);
    }

}