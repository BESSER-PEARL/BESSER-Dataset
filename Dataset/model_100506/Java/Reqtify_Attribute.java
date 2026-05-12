





import java.util.List;
import java.util.ArrayList;

public class Reqtify_Attribute extends TypedElement {

    private String value;



    public Reqtify_Attribute(
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