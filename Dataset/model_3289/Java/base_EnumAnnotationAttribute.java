





import java.util.List;
import java.util.ArrayList;

public class base_EnumAnnotationAttribute extends AnnotationAttribute {

    private String values;



    public base_EnumAnnotationAttribute(
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


}