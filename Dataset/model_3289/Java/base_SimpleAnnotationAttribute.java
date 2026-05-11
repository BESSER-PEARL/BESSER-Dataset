





import java.util.List;
import java.util.ArrayList;

public class base_SimpleAnnotationAttribute extends AnnotationAttribute {

    private String type;



    public base_SimpleAnnotationAttribute(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}