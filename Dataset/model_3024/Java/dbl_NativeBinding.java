





import java.util.List;
import java.util.ArrayList;

public class dbl_NativeBinding  {

    private String targetLanguage;
    private String targetType;





    private dbl_Classifier dbl_classifier;


    public dbl_NativeBinding(
        String targetLanguage,        String targetType    ) {
        this.targetLanguage = targetLanguage;
        this.targetType = targetType;
    }


    public String getTargetlanguage() {
        return targetLanguage;
    }

    public void setTargetlanguage(String targetLanguage) {
        this.targetLanguage = targetLanguage;
    }
    public String getTargettype() {
        return targetType;
    }

    public void setTargettype(String targetType) {
        this.targetType = targetType;
    }

    public dbl_Classifier getDbl_classifier() {
        return dbl_classifier;
    }

    public void setDbl_classifier(dbl_Classifier dbl_classifier) {
        this.dbl_classifier = dbl_classifier;
    }

}