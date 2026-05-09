





import java.util.List;
import java.util.ArrayList;

public class uml_LiteralString extends LiteralSpecification {

    private String value;



    public uml_LiteralString(
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