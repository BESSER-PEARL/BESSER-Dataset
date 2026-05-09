





import java.util.List;
import java.util.ArrayList;

public class java_AnnotableAndModifiable extends Commentable {






    private List<java_AnnotationInstanceOrModifier> java_annotationinstanceormodifiers;


    public java_AnnotableAndModifiable(
    ) {
        super(
        );
        this.java_annotationinstanceormodifiers = new ArrayList<>();
    }

    public java_AnnotableAndModifiable(
        ArrayList<java_AnnotationInstanceOrModifier> java_annotationinstanceormodifiers    ) {
        this.java_annotationinstanceormodifiers = java_annotationinstanceormodifiers;
    }


    public List<java_AnnotationInstanceOrModifier> getJava_annotationinstanceormodifiers() {
        return java_annotationinstanceormodifiers;
    }

    public void addJava_annotationinstanceormodifier(Java_annotationinstanceormodifier java_annotationinstanceormodifier) {
        this.java_annotationinstanceormodifiers.add(java_annotationinstanceormodifier);
    }

}