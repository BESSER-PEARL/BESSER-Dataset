





import java.util.List;
import java.util.ArrayList;

public class CD_Package extends Classifier {






    private List<CD_Classifier> cd_classifiers;


    public CD_Package(
    ) {
        super(
        );
        this.cd_classifiers = new ArrayList<>();
    }

    public CD_Package(
        ArrayList<CD_Classifier> cd_classifiers    ) {
        this.cd_classifiers = cd_classifiers;
    }


    public List<CD_Classifier> getCd_classifiers() {
        return cd_classifiers;
    }

    public void addCd_classifier(Cd_classifier cd_classifier) {
        this.cd_classifiers.add(cd_classifier);
    }

}