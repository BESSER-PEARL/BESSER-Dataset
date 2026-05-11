





import java.util.List;
import java.util.ArrayList;

public class alf_STRING_LITERAL extends LITERAL {

    private String value;



    public alf_STRING_LITERAL(
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