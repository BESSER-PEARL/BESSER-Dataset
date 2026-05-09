





import java.util.List;
import java.util.ArrayList;

public class ccsl_annotation_AnnotableElement extends Element {

    private String annotationsKind;



    public ccsl_annotation_AnnotableElement(
        String annotationsKind    ) {
        super(
        );
        this.annotationsKind = annotationsKind;
    }


    public String getAnnotationskind() {
        return annotationsKind;
    }

    public void setAnnotationskind(String annotationsKind) {
        this.annotationsKind = annotationsKind;
    }


}