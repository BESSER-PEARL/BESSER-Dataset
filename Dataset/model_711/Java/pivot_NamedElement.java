





import java.util.List;
import java.util.ArrayList;

public class pivot_NamedElement extends Element, Nameable {

    private String isStatic;
    private String name;





    private List<pivot_Annotation> pivot_annotations;


    public pivot_NamedElement(
        String isStatic,        String name    ) {
        super(
        );
        this.isStatic = isStatic;
        this.name = name;
        this.pivot_annotations = new ArrayList<>();
    }

    public pivot_NamedElement(
        String isStatic,        String name        ArrayList<pivot_Annotation> pivot_annotations    ) {
        this.isStatic = isStatic;
        this.name = name;
        this.pivot_annotations = pivot_annotations;
    }

    public String getIsstatic() {
        return isStatic;
    }

    public void setIsstatic(String isStatic) {
        this.isStatic = isStatic;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<pivot_Annotation> getPivot_annotations() {
        return pivot_annotations;
    }

    public void addPivot_annotation(Pivot_annotation pivot_annotation) {
        this.pivot_annotations.add(pivot_annotation);
    }

}