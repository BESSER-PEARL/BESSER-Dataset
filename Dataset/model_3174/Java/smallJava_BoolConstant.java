





import java.util.List;
import java.util.ArrayList;

public class smallJava_BoolConstant extends SJExpression {

    private String value;



    public smallJava_BoolConstant(
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