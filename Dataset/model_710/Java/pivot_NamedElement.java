





import java.util.List;
import java.util.ArrayList;

public class pivot_NamedElement extends Nameable, Element {

    private String name;
    private String isStatic;





    private List<pivot_Annotation> pivot_annotations;


    public pivot_NamedElement(
        String name,        String isStatic    ) {
        super(
        );
        this.name = name;
        this.isStatic = isStatic;
        this.pivot_annotations = new ArrayList<>();
    }

    public pivot_NamedElement(
        String name,        String isStatic        ArrayList<pivot_Annotation> pivot_annotations    ) {
        this.name = name;
        this.isStatic = isStatic;
        this.pivot_annotations = pivot_annotations;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }

    public List<pivot_Annotation> getPivot_annotations() {
        return pivot_annotations;
    }

    public void addPivot_annotation(Pivot_annotation pivot_annotation) {
        this.pivot_annotations.add(pivot_annotation);
    }

}