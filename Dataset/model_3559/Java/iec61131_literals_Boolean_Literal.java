





import java.util.List;
import java.util.ArrayList;

public class iec61131_literals_Boolean_Literal extends Constant {

    private String value;



    public iec61131_literals_Boolean_Literal(
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