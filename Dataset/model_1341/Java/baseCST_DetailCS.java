





import java.util.List;
import java.util.ArrayList;

public class baseCST_DetailCS extends NamedElementCS {

    private String value;





    private baseCST_AnnotationElementCS basecst_annotationelementcs;


    public baseCST_DetailCS(
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

    public baseCST_AnnotationElementCS getBasecst_annotationelementcs() {
        return basecst_annotationelementcs;
    }

    public void setBasecst_annotationelementcs(baseCST_AnnotationElementCS basecst_annotationelementcs) {
        this.basecst_annotationelementcs = basecst_annotationelementcs;
    }

}