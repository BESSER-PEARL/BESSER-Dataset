





import java.util.List;
import java.util.ArrayList;

public class Documentation_TextualValue extends ParagraphValue {

    private String value;



    public Documentation_TextualValue(
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