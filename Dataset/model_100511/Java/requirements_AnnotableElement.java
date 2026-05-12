





import java.util.List;
import java.util.ArrayList;

public class requirements_AnnotableElement extends BasicElement {






    private List<requirements_Annotation> requirements_annotations;


    public requirements_AnnotableElement(
    ) {
        super(
        );
        this.requirements_annotations = new ArrayList<>();
    }

    public requirements_AnnotableElement(
        ArrayList<requirements_Annotation> requirements_annotations    ) {
        this.requirements_annotations = requirements_annotations;
    }


    public List<requirements_Annotation> getRequirements_annotations() {
        return requirements_annotations;
    }

    public void addRequirements_annotation(Requirements_annotation requirements_annotation) {
        this.requirements_annotations.add(requirements_annotation);
    }

}