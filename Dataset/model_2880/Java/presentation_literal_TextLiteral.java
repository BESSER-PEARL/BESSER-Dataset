





import java.util.List;
import java.util.ArrayList;

public class presentation_literal_TextLiteral extends GeneralLiteral {

    private String value;



    public presentation_literal_TextLiteral(
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