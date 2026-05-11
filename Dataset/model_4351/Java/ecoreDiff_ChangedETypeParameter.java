





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedETypeParameter extends ETypeParameter {






    private List<ecoreDiff_ETypeParameter> ecorediff_etypeparameters;


    public ecoreDiff_ChangedETypeParameter(
    ) {
        super(
        );
        this.ecorediff_etypeparameters = new ArrayList<>();
    }

    public ecoreDiff_ChangedETypeParameter(
        ArrayList<ecoreDiff_ETypeParameter> ecorediff_etypeparameters    ) {
        this.ecorediff_etypeparameters = ecorediff_etypeparameters;
    }


    public List<ecoreDiff_ETypeParameter> getEcorediff_etypeparameters() {
        return ecorediff_etypeparameters;
    }

    public void addEcorediff_etypeparameter(Ecorediff_etypeparameter ecorediff_etypeparameter) {
        this.ecorediff_etypeparameters.add(ecorediff_etypeparameter);
    }

}