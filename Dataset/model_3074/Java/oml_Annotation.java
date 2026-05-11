





import java.util.List;
import java.util.ArrayList;

public class oml_Annotation  {

    private String key;
    private String value;





    private oml_AnnotatedElement oml_annotatedelement;


    public oml_Annotation(
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

    public oml_AnnotatedElement getOml_annotatedelement() {
        return oml_annotatedelement;
    }

    public void setOml_annotatedelement(oml_AnnotatedElement oml_annotatedelement) {
        this.oml_annotatedelement = oml_annotatedelement;
    }

}