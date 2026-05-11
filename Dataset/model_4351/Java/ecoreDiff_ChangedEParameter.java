





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEParameter extends EParameter {






    private List<ecoreDiff_EParameter> ecorediff_eparameters;


    public ecoreDiff_ChangedEParameter(
    ) {
        super(
        );
        this.ecorediff_eparameters = new ArrayList<>();
    }

    public ecoreDiff_ChangedEParameter(
        ArrayList<ecoreDiff_EParameter> ecorediff_eparameters    ) {
        this.ecorediff_eparameters = ecorediff_eparameters;
    }


    public List<ecoreDiff_EParameter> getEcorediff_eparameters() {
        return ecorediff_eparameters;
    }

    public void addEcorediff_eparameter(Ecorediff_eparameter ecorediff_eparameter) {
        this.ecorediff_eparameters.add(ecorediff_eparameter);
    }

}