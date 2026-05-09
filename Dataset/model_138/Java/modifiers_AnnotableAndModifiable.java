





import java.util.List;
import java.util.ArrayList;

public class modifiers_AnnotableAndModifiable extends Commentable {






    private List<AnnotationInstanceOrModifier> annotationinstanceormodifiers;


    public modifiers_AnnotableAndModifiable(
    ) {
        super(
        );
        this.annotationinstanceormodifiers = new ArrayList<>();
    }

    public modifiers_AnnotableAndModifiable(
        ArrayList<AnnotationInstanceOrModifier> annotationinstanceormodifiers    ) {
        this.annotationinstanceormodifiers = annotationinstanceormodifiers;
    }


    public List<AnnotationInstanceOrModifier> getAnnotationinstanceormodifiers() {
        return annotationinstanceormodifiers;
    }

    public void addAnnotationinstanceormodifier(Annotationinstanceormodifier annotationinstanceormodifier) {
        this.annotationinstanceormodifiers.add(annotationinstanceormodifier);
    }

}