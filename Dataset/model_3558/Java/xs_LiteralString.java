





import java.util.List;
import java.util.ArrayList;

public class xs_LiteralString extends Literal {

    private String value;



    public xs_LiteralString(
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