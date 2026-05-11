





import java.util.List;
import java.util.ArrayList;

public class dbl_AnnotationItem  {

    private String key;
    private String value;





    private dbl_Annotation dbl_annotation;


    public dbl_AnnotationItem(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public dbl_Annotation getDbl_annotation() {
        return dbl_annotation;
    }

    public void setDbl_annotation(dbl_Annotation dbl_annotation) {
        this.dbl_annotation = dbl_annotation;
    }

}