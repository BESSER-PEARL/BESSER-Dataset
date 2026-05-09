





import java.util.List;
import java.util.ArrayList;

public class ccsl_variable_FieldVariable extends variable_InitializableVariable, annotation_AnnotableElement {

    private String static;
    private String visibility;



    public ccsl_variable_FieldVariable(
        String static,        String visibility    ) {
        super(
        );
        this.static = static;
        this.visibility = visibility;
    }


    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}