





import java.util.List;
import java.util.ArrayList;

public class UMLModel_LiteralBoolean extends LiteralSpecification {

    private String value;



    public UMLModel_LiteralBoolean(
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