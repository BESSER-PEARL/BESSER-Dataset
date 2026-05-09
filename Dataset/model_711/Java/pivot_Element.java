





import java.util.List;
import java.util.ArrayList;

public class pivot_Element extends Visitable {






    private pivot_Annotation pivot_annotation;




    private pivot_Annotation pivot_annotation;




    private pivot_Constraint pivot_constraint;




    private List<pivot_ElementExtension> pivot_elementextensions;




    private pivot_ElementExtension pivot_elementextension;


    public pivot_Element(
    ) {
        super(
        );
        this.pivot_elementextensions = new ArrayList<>();
    }

    public pivot_Element(
        ArrayList<pivot_ElementExtension> pivot_elementextensions    ) {
        this.pivot_elementextensions = pivot_elementextensions;
    }


    public pivot_Annotation getPivot_annotation() {
        return pivot_annotation;
    }

    public void setPivot_annotation(pivot_Annotation pivot_annotation) {
        this.pivot_annotation = pivot_annotation;
    }
    public pivot_Annotation getPivot_annotation() {
        return pivot_annotation;
    }

    public void setPivot_annotation(pivot_Annotation pivot_annotation) {
        this.pivot_annotation = pivot_annotation;
    }
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }
    public List<pivot_ElementExtension> getPivot_elementextensions() {
        return pivot_elementextensions;
    }

    public void addPivot_elementextension(Pivot_elementextension pivot_elementextension) {
        this.pivot_elementextensions.add(pivot_elementextension);
    }
    public pivot_ElementExtension getPivot_elementextension() {
        return pivot_elementextension;
    }

    public void setPivot_elementextension(pivot_ElementExtension pivot_elementextension) {
        this.pivot_elementextension = pivot_elementextension;
    }

}