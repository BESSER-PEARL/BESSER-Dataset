





import java.util.List;
import java.util.ArrayList;

public class Java5_BodyDeclaration extends NamedElement {






    private List<Java5_Annotation> java5_annotations;


    public Java5_BodyDeclaration(
    ) {
        super(
        );
        this.java5_annotations = new ArrayList<>();
    }

    public Java5_BodyDeclaration(
        ArrayList<Java5_Annotation> java5_annotations    ) {
        this.java5_annotations = java5_annotations;
    }


    public List<Java5_Annotation> getJava5_annotations() {
        return java5_annotations;
    }

    public void addJava5_annotation(Java5_annotation java5_annotation) {
        this.java5_annotations.add(java5_annotation);
    }

}