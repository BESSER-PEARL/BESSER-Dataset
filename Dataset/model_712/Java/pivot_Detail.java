





import java.util.List;
import java.util.ArrayList;

public class pivot_Detail extends NamedElement {

    private String value;





    private pivot_Annotation pivot_annotation;


    public pivot_Detail(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public pivot_Annotation getPivot_annotation() {
        return pivot_annotation;
    }

    public void setPivot_annotation(pivot_Annotation pivot_annotation) {
        this.pivot_annotation = pivot_annotation;
    }

}