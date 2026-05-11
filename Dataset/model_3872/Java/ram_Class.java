





import java.util.List;
import java.util.ArrayList;

public class ram_Class extends Classifier {

    private boolean abstract;
    private boolean partial;





    private List<ram_Classifier> ram_classifiers;


    public ram_Class(
        boolean abstract,        boolean partial    ) {
        super(
        );
        this.abstract = abstract;
        this.partial = partial;
        this.ram_classifiers = new ArrayList<>();
    }

    public ram_Class(
        boolean abstract,        boolean partial        ArrayList<ram_Classifier> ram_classifiers    ) {
        this.abstract = abstract;
        this.partial = partial;
        this.ram_classifiers = ram_classifiers;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public boolean getPartial() {
        return partial;
    }

    public void setPartial(boolean partial) {
        this.partial = partial;
    }

    public List<ram_Classifier> getRam_classifiers() {
        return ram_classifiers;
    }

    public void addRam_classifier(Ram_classifier ram_classifier) {
        this.ram_classifiers.add(ram_classifier);
    }

}