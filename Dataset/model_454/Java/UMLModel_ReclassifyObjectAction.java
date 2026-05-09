





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ReclassifyObjectAction extends Action {

    private String newClassifier;
    private String oldClassifier;
    private String isReplaceAll;



    public UMLModel_ReclassifyObjectAction(
        String newClassifier,        String oldClassifier,        String isReplaceAll    ) {
        super(
        );
        this.newClassifier = newClassifier;
        this.oldClassifier = oldClassifier;
        this.isReplaceAll = isReplaceAll;
    }


    public String getNewclassifier() {
        return newClassifier;
    }

    public void setNewclassifier(String newClassifier) {
        this.newClassifier = newClassifier;
    }
    public String getOldclassifier() {
        return oldClassifier;
    }

    public void setOldclassifier(String oldClassifier) {
        this.oldClassifier = oldClassifier;
    }
    public String getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(String isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }


}