





import java.util.List;
import java.util.ArrayList;

public class Core_Feature extends ModelElement {

    private String ownerScope;





    private Classifier classifier;


    public Core_Feature(
        String ownerScope    ) {
        super(
        );
        this.ownerScope = ownerScope;
    }


    public String getOwnerscope() {
        return ownerScope;
    }

    public void setOwnerscope(String ownerScope) {
        this.ownerScope = ownerScope;
    }

    public Classifier getClassifier() {
        return classifier;
    }

    public void setClassifier(Classifier classifier) {
        this.classifier = classifier;
    }

}