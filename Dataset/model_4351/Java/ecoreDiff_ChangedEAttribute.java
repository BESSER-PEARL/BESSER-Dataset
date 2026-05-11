





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEAttribute extends EAttribute {






    private List<ecoreDiff_EAttribute> ecorediff_eattributes;


    public ecoreDiff_ChangedEAttribute(
    ) {
        super(
        );
        this.ecorediff_eattributes = new ArrayList<>();
    }

    public ecoreDiff_ChangedEAttribute(
        ArrayList<ecoreDiff_EAttribute> ecorediff_eattributes    ) {
        this.ecorediff_eattributes = ecorediff_eattributes;
    }


    public List<ecoreDiff_EAttribute> getEcorediff_eattributes() {
        return ecorediff_eattributes;
    }

    public void addEcorediff_eattribute(Ecorediff_eattribute ecorediff_eattribute) {
        this.ecorediff_eattributes.add(ecorediff_eattribute);
    }

}