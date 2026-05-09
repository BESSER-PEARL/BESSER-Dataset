





import java.util.List;
import java.util.ArrayList;

public class pivot_Element extends Visitable {






    private pivot_Annotation pivot_annotation;




    private pivot_Annotation pivot_annotation;




    private List<pivot_Element> pivot_elements;




    private pivot_Constraint pivot_constraint;


    public pivot_Element(
    ) {
        super(
        );
        this.pivot_elements = new ArrayList<>();
    }

    public pivot_Element(
        ArrayList<pivot_Element> pivot_elements    ) {
        this.pivot_elements = pivot_elements;
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
    public List<pivot_Element> getPivot_elements() {
        return pivot_elements;
    }

    public void addPivot_element(Pivot_element pivot_element) {
        this.pivot_elements.add(pivot_element);
    }
    public pivot_Constraint getPivot_constraint() {
        return pivot_constraint;
    }

    public void setPivot_constraint(pivot_Constraint pivot_constraint) {
        this.pivot_constraint = pivot_constraint;
    }

}