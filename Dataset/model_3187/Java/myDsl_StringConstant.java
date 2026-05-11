





import java.util.List;
import java.util.ArrayList;

public class myDsl_StringConstant extends Expression {

    private String value;



    public myDsl_StringConstant(
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