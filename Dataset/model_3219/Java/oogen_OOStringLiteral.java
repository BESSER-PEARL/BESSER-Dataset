





import java.util.List;
import java.util.ArrayList;

public class oogen_OOStringLiteral extends OOExpression {

    private String value;



    public oogen_OOStringLiteral(
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