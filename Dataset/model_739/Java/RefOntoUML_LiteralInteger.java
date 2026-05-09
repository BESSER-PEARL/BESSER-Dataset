





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_LiteralInteger extends LiteralSpecification {

    private String value;



    public RefOntoUML_LiteralInteger(
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