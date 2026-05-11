





import java.util.List;
import java.util.ArrayList;

public class dbl_NativeBinding  {

    private String targetType;
    private String targetLanguage;





    private dbl_Class dbl_class;


    public dbl_NativeBinding(
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

    public dbl_Class getDbl_class() {
        return dbl_class;
    }

    public void setDbl_class(dbl_Class dbl_class) {
        this.dbl_class = dbl_class;
    }

}