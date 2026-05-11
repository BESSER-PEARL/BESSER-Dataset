





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEFactory extends EFactory {






    private List<ecoreDiff_EFactory> ecorediff_efactorys;


    public ecoreDiff_ChangedEFactory(
    ) {
        super(
        );
        this.ecorediff_efactorys = new ArrayList<>();
    }

    public ecoreDiff_ChangedEFactory(
        ArrayList<ecoreDiff_EFactory> ecorediff_efactorys    ) {
        this.ecorediff_efactorys = ecorediff_efactorys;
    }


    public List<ecoreDiff_EFactory> getEcorediff_efactorys() {
        return ecorediff_efactorys;
    }

    public void addEcorediff_efactory(Ecorediff_efactory ecorediff_efactory) {
        this.ecorediff_efactorys.add(ecorediff_efactory);
    }

}