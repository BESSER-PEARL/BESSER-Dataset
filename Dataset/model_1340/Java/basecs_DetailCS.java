





import java.util.List;
import java.util.ArrayList;

public class basecs_DetailCS extends NamedElementCS {

    private String value;





    private basecs_AnnotationElementCS basecs_annotationelementcs;


    public basecs_DetailCS(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public basecs_AnnotationElementCS getBasecs_annotationelementcs() {
        return basecs_annotationelementcs;
    }

    public void setBasecs_annotationelementcs(basecs_AnnotationElementCS basecs_annotationelementcs) {
        this.basecs_annotationelementcs = basecs_annotationelementcs;
    }

}