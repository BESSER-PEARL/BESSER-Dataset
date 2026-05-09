





import java.util.List;
import java.util.ArrayList;

public class java_AnnotationInstance extends NamespaceAwareElement, AnnotationInstanceOrModifier, Reference {






    private java_Annotable java_annotable;




    private java_AnnotationParameter java_annotationparameter;


    public java_AnnotationInstance(
    ) {
        super(
        );
    }



    public java_Annotable getJava_annotable() {
        return java_annotable;
    }

    public void setJava_annotable(java_Annotable java_annotable) {
        this.java_annotable = java_annotable;
    }
    public java_AnnotationParameter getJava_annotationparameter() {
        return java_annotationparameter;
    }

    public void setJava_annotationparameter(java_AnnotationParameter java_annotationparameter) {
        this.java_annotationparameter = java_annotationparameter;
    }

}