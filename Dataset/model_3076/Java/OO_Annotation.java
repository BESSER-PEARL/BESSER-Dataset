





import java.util.List;
import java.util.ArrayList;

public class OO_Annotation  {

    private String key;
    private String value;





    private OO_AnnotatedElement oo_annotatedelement;


    public OO_Annotation(
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

    public OO_AnnotatedElement getOo_annotatedelement() {
        return oo_annotatedelement;
    }

    public void setOo_annotatedelement(OO_AnnotatedElement oo_annotatedelement) {
        this.oo_annotatedelement = oo_annotatedelement;
    }

}