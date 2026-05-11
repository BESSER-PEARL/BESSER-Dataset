





import java.util.List;
import java.util.ArrayList;

public class frontend_core_StringLiteral extends Expression {

    private String value;



    public frontend_core_StringLiteral(
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