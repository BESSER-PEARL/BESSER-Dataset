





import java.util.List;
import java.util.ArrayList;

public class vcml_NumericLiteral extends NumberListEntry, Literal {

    private String value;



    public vcml_NumericLiteral(
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