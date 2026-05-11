





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEEnum extends EEnum {






    private List<ecoreDiff_EEnum> ecorediff_eenums;


    public ecoreDiff_ChangedEEnum(
    ) {
        super(
        );
        this.ecorediff_eenums = new ArrayList<>();
    }

    public ecoreDiff_ChangedEEnum(
        ArrayList<ecoreDiff_EEnum> ecorediff_eenums    ) {
        this.ecorediff_eenums = ecorediff_eenums;
    }


    public List<ecoreDiff_EEnum> getEcorediff_eenums() {
        return ecorediff_eenums;
    }

    public void addEcorediff_eenum(Ecorediff_eenum ecorediff_eenum) {
        this.ecorediff_eenums.add(ecorediff_eenum);
    }

}