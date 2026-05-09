





import java.util.List;
import java.util.ArrayList;

public class pivot_ConstructorExp extends OCLExpression {

    private String value;



    public pivot_ConstructorExp(
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