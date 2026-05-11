





import java.util.List;
import java.util.ArrayList;

public class ir_AnnotationArgument  {

    private String value;
    private String id;





    private ir_Annotation ir_annotation;


    public ir_AnnotationArgument(
        String value,        String id    ) {
        this.value = value;
        this.id = id;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public ir_Annotation getIr_annotation() {
        return ir_annotation;
    }

    public void setIr_annotation(ir_Annotation ir_annotation) {
        this.ir_annotation = ir_annotation;
    }

}