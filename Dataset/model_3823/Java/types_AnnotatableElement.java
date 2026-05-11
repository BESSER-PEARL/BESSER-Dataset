





import java.util.List;
import java.util.ArrayList;

public class types_AnnotatableElement  {






    private List<types_Annotation> types_annotations;


    public types_AnnotatableElement(
    ) {
        this.types_annotations = new ArrayList<>();
    }

    public types_AnnotatableElement(
        ArrayList<types_Annotation> types_annotations    ) {
        this.types_annotations = types_annotations;
    }


    public List<types_Annotation> getTypes_annotations() {
        return types_annotations;
    }

    public void addTypes_annotation(Types_annotation types_annotation) {
        this.types_annotations.add(types_annotation);
    }

}