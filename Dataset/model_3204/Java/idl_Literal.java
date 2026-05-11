





import java.util.List;
import java.util.ArrayList;

public class idl_Literal extends PrimaryExpr {

    private String value;



    public idl_Literal(
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