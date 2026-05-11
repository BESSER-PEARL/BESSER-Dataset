





import java.util.List;
import java.util.ArrayList;

public class typedef_TDAnnotationDetail  {

    private String value;
    private String key;





    private typedef_TypeAnnotation typedef_typeannotation;


    public typedef_TDAnnotationDetail(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public typedef_TypeAnnotation getTypedef_typeannotation() {
        return typedef_typeannotation;
    }

    public void setTypedef_typeannotation(typedef_TypeAnnotation typedef_typeannotation) {
        this.typedef_typeannotation = typedef_typeannotation;
    }

}