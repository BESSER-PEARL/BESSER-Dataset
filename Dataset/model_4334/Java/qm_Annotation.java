





import java.util.List;
import java.util.ArrayList;

public class qm_Annotation  {

    private String key;
    private String value;





    private qm_AnnotatedElement qm_annotatedelement;


    public qm_Annotation(
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

    public qm_AnnotatedElement getQm_annotatedelement() {
        return qm_annotatedelement;
    }

    public void setQm_annotatedelement(qm_AnnotatedElement qm_annotatedelement) {
        this.qm_annotatedelement = qm_annotatedelement;
    }

}