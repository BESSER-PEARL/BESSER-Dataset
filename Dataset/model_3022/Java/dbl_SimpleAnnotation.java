





import java.util.List;
import java.util.ArrayList;

public class dbl_SimpleAnnotation extends NamedElement {

    private String value;



    public dbl_SimpleAnnotation(
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


}