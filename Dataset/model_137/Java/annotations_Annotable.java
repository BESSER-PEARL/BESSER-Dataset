





import java.util.List;
import java.util.ArrayList;

public class annotations_Annotable extends Commentable {






    private List<AnnotationInstance> annotationinstances;


    public annotations_Annotable(
    ) {
        super(
        );
        this.annotationinstances = new ArrayList<>();
    }

    public annotations_Annotable(
        ArrayList<AnnotationInstance> annotationinstances    ) {
        this.annotationinstances = annotationinstances;
    }


    public List<AnnotationInstance> getAnnotationinstances() {
        return annotationinstances;
    }

    public void addAnnotationinstance(Annotationinstance annotationinstance) {
        this.annotationinstances.add(annotationinstance);
    }

}