





import java.util.List;
import java.util.ArrayList;

public class java_AnnotationParameterList extends AnnotationParameter {






    private List<java_AnnotationAttributeSetting> java_annotationattributesettings;


    public java_AnnotationParameterList(
    ) {
        super(
        );
        this.java_annotationattributesettings = new ArrayList<>();
    }

    public java_AnnotationParameterList(
        ArrayList<java_AnnotationAttributeSetting> java_annotationattributesettings    ) {
        this.java_annotationattributesettings = java_annotationattributesettings;
    }


    public List<java_AnnotationAttributeSetting> getJava_annotationattributesettings() {
        return java_annotationattributesettings;
    }

    public void addJava_annotationattributesetting(Java_annotationattributesetting java_annotationattributesetting) {
        this.java_annotationattributesettings.add(java_annotationattributesetting);
    }

}