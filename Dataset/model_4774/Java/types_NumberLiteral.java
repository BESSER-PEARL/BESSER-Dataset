





import java.util.List;
import java.util.ArrayList;

public class types_NumberLiteral extends Literal {

    private String value;



    public types_NumberLiteral(
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