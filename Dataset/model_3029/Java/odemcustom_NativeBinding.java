





import java.util.List;
import java.util.ArrayList;

public class odemcustom_NativeBinding  {

    private String targetType;
    private String targetLanguage;





    private odemcustom_Classifier odemcustom_classifier;


    public odemcustom_NativeBinding(
        String targetType,        String targetLanguage    ) {
        this.targetType = targetType;
        this.targetLanguage = targetLanguage;
    }


    public String getTargettype() {
        return targetType;
    }

    public void setTargettype(String targetType) {
        this.targetType = targetType;
    }
    public String getTargetlanguage() {
        return targetLanguage;
    }

    public void setTargetlanguage(String targetLanguage) {
        this.targetLanguage = targetLanguage;
    }

    public odemcustom_Classifier getOdemcustom_classifier() {
        return odemcustom_classifier;
    }

    public void setOdemcustom_classifier(odemcustom_Classifier odemcustom_classifier) {
        this.odemcustom_classifier = odemcustom_classifier;
    }

}