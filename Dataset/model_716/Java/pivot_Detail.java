





import java.util.List;
import java.util.ArrayList;

public class pivot_Detail extends NamedElement {

    private String values;





    private pivot_Annotation pivot_annotation;


    public pivot_Detail(
        String values    ) {
        super(
        );
        this.values = values;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }

    public pivot_Annotation getPivot_annotation() {
        return pivot_annotation;
    }

    public void setPivot_annotation(pivot_Annotation pivot_annotation) {
        this.pivot_annotation = pivot_annotation;
    }

}