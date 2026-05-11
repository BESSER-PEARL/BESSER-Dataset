





import java.util.List;
import java.util.ArrayList;

public class shape_TextBody  {

    private String value;





    private shape_Description shape_description;


    public shape_TextBody(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public shape_Description getShape_description() {
        return shape_description;
    }

    public void setShape_description(shape_Description shape_description) {
        this.shape_description = shape_description;
    }

}