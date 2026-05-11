





import java.util.List;
import java.util.ArrayList;

public class pp2_LiteralName extends LiteralExpression {

    private String value;



    public pp2_LiteralName(
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