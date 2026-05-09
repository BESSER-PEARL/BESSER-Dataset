





import java.util.List;
import java.util.ArrayList;

public class annotations_AnnotationInstance extends NamespaceAwareElement, Reference, AnnotationInstanceOrModifier {






    private AnnotationParameter annotationparameter;


    public annotations_AnnotationInstance(
    ) {
        super(
        );
    }



    public AnnotationParameter getAnnotationparameter() {
        return annotationparameter;
    }

    public void setAnnotationparameter(AnnotationParameter annotationparameter) {
        this.annotationparameter = annotationparameter;
    }

}