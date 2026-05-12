





import java.util.List;
import java.util.ArrayList;

public class Core_Parameter extends ModelElement {

    private String kind;





    private Classifier classifier;


    public Core_Parameter(
        String kind    ) {
        super(
        );
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public Classifier getClassifier() {
        return classifier;
    }

    public void setClassifier(Classifier classifier) {
        this.classifier = classifier;
    }

}