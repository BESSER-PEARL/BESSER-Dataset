





import java.util.List;
import java.util.ArrayList;

public class UMLModel_CreateObjectAction extends Action {

    private String classifier;



    public UMLModel_CreateObjectAction(
        String classifier    ) {
        super(
        );
        this.classifier = classifier;
    }


    public String getClassifier() {
        return classifier;
    }

    public void setClassifier(String classifier) {
        this.classifier = classifier;
    }


}