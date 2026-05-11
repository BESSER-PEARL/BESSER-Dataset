





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEPackage extends EPackage {






    private List<ecoreDiff_EPackage> ecorediff_epackages;


    public ecoreDiff_ChangedEPackage(
    ) {
        super(
        );
        this.ecorediff_epackages = new ArrayList<>();
    }

    public ecoreDiff_ChangedEPackage(
        ArrayList<ecoreDiff_EPackage> ecorediff_epackages    ) {
        this.ecorediff_epackages = ecorediff_epackages;
    }


    public List<ecoreDiff_EPackage> getEcorediff_epackages() {
        return ecorediff_epackages;
    }

    public void addEcorediff_epackage(Ecorediff_epackage ecorediff_epackage) {
        this.ecorediff_epackages.add(ecorediff_epackage);
    }

}