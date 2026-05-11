





import java.util.List;
import java.util.ArrayList;

public class ram_LiteralChar extends LiteralSpecification {

    private String value;



    public ram_LiteralChar(
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