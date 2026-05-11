





import java.util.List;
import java.util.ArrayList;

public class typesystem_IntegerLiteral extends NumericLiteral {

    private String value;



    public typesystem_IntegerLiteral(
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