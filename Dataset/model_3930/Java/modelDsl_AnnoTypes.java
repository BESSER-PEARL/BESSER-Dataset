





import java.util.List;
import java.util.ArrayList;

public class modelDsl_AnnoTypes  {

    private String type;





    private modelDsl_Annotation modeldsl_annotation;


    public modelDsl_AnnoTypes(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public modelDsl_Annotation getModeldsl_annotation() {
        return modeldsl_annotation;
    }

    public void setModeldsl_annotation(modelDsl_Annotation modeldsl_annotation) {
        this.modeldsl_annotation = modeldsl_annotation;
    }

}