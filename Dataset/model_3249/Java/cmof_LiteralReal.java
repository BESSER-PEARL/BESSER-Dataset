





import java.util.List;
import java.util.ArrayList;

public class cmof_LiteralReal extends LiteralSpecification {

    private String value;



    public cmof_LiteralReal(
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