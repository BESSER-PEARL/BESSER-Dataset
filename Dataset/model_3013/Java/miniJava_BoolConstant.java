





import java.util.List;
import java.util.ArrayList;

public class miniJava_BoolConstant extends Expression {

    private String value;



    public miniJava_BoolConstant(
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