





import java.util.List;
import java.util.ArrayList;

public class requirement_TextAttribute extends Attribute {

    private String value;



    public requirement_TextAttribute(
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